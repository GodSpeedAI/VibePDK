#!/usr/bin/env python
"""
translator.py - A deterministic transformer for architecture and techstack specifications.

This script provides two main functionalities:
1.  Translate between CALM (Cloud Application Lifecycle Management) JSON format
    and a domain-specific YAML format used by Nx generators. This allows keeping
    architecture diagrams and domain models in sync.
2.  Process a `techstack.yaml` file to produce a normalized, deterministic JSON
    representation for downstream tooling. This includes planning (diff) and
    applying changes.

All outputs are deterministic to support snapshot testing and reproducible builds.

Usage:
    - CALM/Domain Translation:
        python translator.py calm-to-domain <calm.json> <domain.yaml>
        python translator.py domain-to-calm <domain.yaml> <calm.json>

    - Techstack Processing:
        python translator.py techstack plan [path/to/techstack.yaml]
        python translator.py techstack apply [--dry-run] [path/to/techstack.yaml]

See docs/ for more details on the mapping specifications.
"""

import argparse
import difflib
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, cast

import yaml

# Type Aliases for clarity
JsonDict = Dict[str, Any]
CalmDict = JsonDict
DomainDict = JsonDict
TechstackDict = JsonDict
YamlDict = JsonDict


# --- File I/O Helpers ---


def _read_json(p: Path) -> JsonDict:
    """Reads a JSON file."""
    with p.open("r", encoding="utf-8") as f:
        return cast(JsonDict, json.load(f))


def _write_json(p: Path, data: JsonDict) -> None:
    """Writes data to a JSON file with consistent formatting."""
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("
")


def _read_yaml(p: Path) -> YamlDict:
    """Reads a YAML file, ensuring it's a dictionary."""
    with p.open("r", encoding="utf-8") as f:
        content = yaml.safe_load(f)
        if not isinstance(content, dict):
            raise TypeError(f"Expected a dictionary in {p}, but got {type(content)}")
        return cast(YamlDict, content)


# --- CALM <-> Domain Translation ---


def calm_to_domain(calm_path: Path, domain_path: Path) -> None:
    """Convert CALM JSON to domain YAML."""
    calm = _read_json(calm_path)
    domain: DomainDict = {"services": [], "relationships": []}

    for node in calm.get("nodes", []):
        service = {
            "name": node["id"],
            "description": node.get("description", ""),
            "entities": [],
        }
        domain["services"].append(service)

    for rel in calm.get("relationships", []):
        domain["relationships"].append(
            {
                "from": rel["source"],
                "to": rel["target"],
                "type": rel.get("type", "depends_on"),
            }
        )

    with domain_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(domain, f, sort_keys=False)
    print(f"Generated domain YAML at {domain_path}")


def domain_to_calm(domain_path: Path, calm_path: Path) -> None:
    """Convert domain YAML to CALM JSON."""
    domain = _read_yaml(domain_path)
    calm: CalmDict = {"nodes": [], "relationships": []}

    for svc in domain.get("services", []):
        node = {"id": svc["name"], "description": svc.get("description", "")}
        calm["nodes"].append(node)

    for rel in domain.get("relationships", []):
        calm["relationships"].append(
            {
                "source": rel["from"],
                "target": rel["to"],
                "type": rel.get("type", "depends_on"),
            }
        )

    with calm_path.open("w", encoding="utf-8") as f:
        json.dump(calm, f, indent=2)
    print(f"Generated CALM JSON at {calm_path}")


# --- Techstack Processing ---


def _validate_against_schema_minimal(data: TechstackDict) -> None:
    """
    Performs minimal structural validation on techstack data.

    This is a basic check and does not replace a full schema validation.
    """
    if not isinstance(data, dict) or not data:
        raise ValueError("Techstack data must be a non-empty dictionary.")

    # Optional: ensure some expected categories when present are objects or lists
    for k in [
        "core_application_dependencies",
        "infrastructure_runtime_dependencies",
        "data_layer_dependencies",
        "development_only_dependencies",
        "build_deployment_dependencies",
        "monitoring_observability_dependencies",
        "security_dependencies",
        "frontend_client_dependencies",
        "communication_integration_dependencies",
        "utility_helper_dependencies",
        "implementation_priority",
    ]:
        if k in data and not isinstance(data[k], (dict, list)):
            raise ValueError(f"Techstack key '{k}' must be an object or list.")


def _normalize_stack(stack: TechstackDict) -> JsonDict:
    """
    Produces a compact, normalized, and deterministic view of the techstack.
    """

    def sorted_items(obj: Any) -> Any:
        if isinstance(obj, dict):
            return {k: sorted_items(obj[k]) for k in sorted(obj.keys())}
        if isinstance(obj, list):
            # Sort list of dicts by a stable JSON representation
            try:
                return sorted(
                    [sorted_items(x) for x in obj],
                    key=lambda x: json.dumps(x, sort_keys=True),
                )
            except TypeError:  # Handle lists with un-sortable/un-serializable items
                return [sorted_items(x) for x in obj]
        return obj

    out: JsonDict = {
        "meta": {"source": "techstack.yaml", "version": 1},
        "categories": {},
    }
    # Ensure categories are sorted for deterministic output
    for cat in sorted(stack.keys()):
        out["categories"][cat] = sorted_items(stack[cat])
    return out


def _process_techstack(ts_path: Path, repo_root: Path) -> tuple[JsonDict, Path]:
    """Loads, validates, and normalizes the techstack file."""
    # Schema validation is optional, as the schema might not be present.
    schema_path = repo_root / "docs" / "techstack.schema.json"
    if not schema_path.exists():
        print(
            f"warning: schema not found at {schema_path}, proceeding with minimal checks"
        )

    stack = _read_yaml(ts_path)
    _validate_against_schema_minimal(stack)

    resolved = _normalize_stack(stack)

    derived_dir = Path(__file__).resolve().parent / ".derived"
    resolved_path = derived_dir / "techstack.resolved.json"

    return resolved, resolved_path


def _show_diff(before: JsonDict, after: JsonDict, path: Path) -> bool:
    """Compares two dictionaries and prints a unified diff. Returns True if different."""
    before_str = json.dumps(before, indent=2, sort_keys=True).splitlines(keepends=True)
    after_str = json.dumps(after, indent=2, sort_keys=True).splitlines(keepends=True)

    diff = list(
        difflib.unified_diff(before_str, after_str, fromfile=str(path), tofile=str(path))
    )

    if diff:
        sys.stdout.write("".join(diff))
        return True

    print("No changes.")
    return False


def techstack_plan(ts_path: Path, repo_root: Path) -> None:
    """Shows a diff of what changes would be made by 'apply'."""
    resolved, resolved_path = _process_techstack(ts_path, repo_root)
    before = _read_json(resolved_path) if resolved_path.exists() else {}
    _show_diff(before, resolved, resolved_path)


def techstack_apply(ts_path: Path, repo_root: Path, dry_run: bool = False) -> None:
    """Applies changes to the derived techstack file."""
    resolved, resolved_path = _process_techstack(ts_path, repo_root)

    if dry_run:
        before = _read_json(resolved_path) if resolved_path.exists() else {}
        has_changes = _show_diff(before, resolved, resolved_path)
        if has_changes:
            print(f"
[dry-run] Would write changes to {resolved_path}")
        return

    _write_json(resolved_path, resolved)
    print(f"Wrote {resolved_path}")


# --- Main CLI ---


def main() -> None:
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Translate between CALM JSON and domain YAML, or process techstack files.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Sub-command help"
    )

    # --- calm-to-domain ---
    parser_c2d = subparsers.add_parser(
        "calm-to-domain", help="Convert CALM JSON to domain YAML."
    )
    parser_c2d.add_argument(
        "from_calm", type=Path, help="Path to input CALM JSON file."
    )
    parser_c2d.add_argument(
        "to_domain", type=Path, help="Path to output domain YAML file."
    )

    # --- domain-to-calm ---
    parser_d2c = subparsers.add_parser(
        "domain-to-calm", help="Convert domain YAML to CALM JSON."
    )
    parser_d2c.add_argument(
        "from_domain", type=Path, help="Path to input domain YAML file."
    )
    parser_d2c.add_argument("to_calm", type=Path, help="Path to output CALM JSON file.")

    # --- techstack ---
    parser_techstack = subparsers.add_parser(
        "techstack", help="Plan or apply techstack changes."
    )
    techstack_subparsers = parser_techstack.add_subparsers(
        dest="subcommand", required=True, help="Techstack action"
    )

    # techstack plan
    parser_plan = techstack_subparsers.add_parser(
        "plan", help="Show a diff of proposed techstack changes."
    )
    parser_plan.add_argument(
        "ts_path",
        type=Path,
        nargs="?",
        default="techstack.yaml",
        help="Path to techstack.yaml file (default: ./techstack.yaml)",
    )

    # techstack apply
    parser_apply = techstack_subparsers.add_parser(
        "apply", help="Apply changes to the derived techstack file."
    )
    parser_apply.add_argument(
        "ts_path",
        type=Path,
        nargs="?",
        default="techstack.yaml",
        help="Path to techstack.yaml file (default: ./techstack.yaml)",
    )
    parser_apply.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes.",
    )

    args = parser.parse_args()

    try:
        if args.command == "calm-to-domain":
            calm_to_domain(args.from_calm, args.to_domain)
        elif args.command == "domain-to-calm":
            domain_to_calm(args.from_domain, args.to_calm)
        elif args.command == "techstack":
            # For simplicity, assuming script is run from repo root.
            repo_root = Path.cwd()
            ts_path = args.ts_path.resolve()

            if not ts_path.exists():
                raise FileNotFoundError(f"Techstack file not found at {ts_path}")

            if args.subcommand == "plan":
                techstack_plan(ts_path, repo_root)
            elif args.subcommand == "apply":
                techstack_apply(ts_path, repo_root, dry_run=args.dry_run)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()