#!/usr/bin/env python
"""
translator.py - A deterministic transformer between CALM JSON and domain.yaml specifications.

This script can convert a CALM architecture description into a domain model YAML used by
the @nxlv/python Nx generator, and vice versa. It relies on simple deterministic
templating and does not embed timestamps or nondeterministic values. This makes
outputs suitable for snapshot testing and reproducible builds.

Usage:
    python translator.py --from-calm path/to/system.calm.json --to-domain path/to/domain.yaml
    python translator.py --from-domain path/to/domain.yaml --to-calm path/to/system.calm.json

The conversion logic here is intentionally simple: it maps CALM nodes to domain
entities and interfaces to service relations. You can extend this script to
support additional CALM semantics (controls, patterns) or more complex domain
fields. See docs/ for the mapping specification.
"""

import argparse
import json
import yaml
from pathlib import Path


def calm_to_domain(calm_path: Path, domain_path: Path) -> None:
    """Convert CALM JSON to domain YAML."""
    with calm_path.open() as f:
        calm = json.load(f)
    domain = {
        'services': [],
        'relationships': []
    }
    for node in calm.get('nodes', []):
        service = {
            'name': node['id'],
            'description': node.get('description', ''),
            'entities': []
        }
        domain['services'].append(service)
    for rel in calm.get('relationships', []):
        domain['relationships'].append({
            'from': rel['source'],
            'to': rel['target'],
            'type': rel.get('type', 'depends_on')
        })
    with domain_path.open('w') as f:
        yaml.safe_dump(domain, f, sort_keys=False)
    print(f"Generated domain YAML at {domain_path}")


def domain_to_calm(domain_path: Path, calm_path: Path) -> None:
    """Convert domain YAML to CALM JSON."""
    with domain_path.open() as f:
        domain = yaml.safe_load(f)
    calm = {
        'nodes': [],
        'relationships': []
    }
    for svc in domain.get('services', []):
        node = {
            'id': svc['name'],
            'description': svc.get('description', '')
        }
        calm['nodes'].append(node)
    for rel in domain.get('relationships', []):
        calm['relationships'].append({
            'source': rel['from'],
            'target': rel['to'],
            'type': rel.get('type', 'depends_on')
        })
    with calm_path.open('w') as f:
        json.dump(calm, f, indent=2)
    print(f"Generated CALM JSON at {calm_path}")


def main():
    parser = argparse.ArgumentParser(description='Translate between CALM JSON and domain YAML.')
    parser.add_argument('--from-calm', type=str, help='Path to input CALM JSON')
    parser.add_argument('--to-domain', type=str, help='Path to output domain YAML')
    parser.add_argument('--from-domain', type=str, help='Path to input domain YAML')
    parser.add_argument('--to-calm', type=str, help='Path to output CALM JSON')
    args = parser.parse_args()
    if args.from_calm and args.to_domain:
        calm_to_domain(Path(args.from_calm), Path(args.to_domain))
    elif args.from_domain and args.to_calm:
        domain_to_calm(Path(args.from_domain), Path(args.to_calm))
    else:
        parser.error('You must specify either --from-calm with --to-domain or --from-domain with --to-calm.')


if __name__ == '__main__':
    main()