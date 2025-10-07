from __future__ import annotations

import json
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "0.1.0"


def _load_package_version(package_path: Path) -> str:
    with package_path.open("r", encoding="utf-8") as handle:
        package_data = json.load(handle)
    version = package_data.get("version")
    if not isinstance(version, str):
        raise AssertionError(f"Missing string version in {package_path!s}")
    return version


def _load_pyproject_version(pyproject_path: Path) -> str:
    with pyproject_path.open("rb") as handle:
        pyproject_data = tomllib.load(handle)
    project = pyproject_data.get("project", {})
    version = project.get("version")
    if not isinstance(version, str):
        raise AssertionError(f"Missing string version in {pyproject_path!s}")
    return version


def test_release_version_alignment() -> None:
    root_package_version = _load_package_version(REPO_ROOT / "package.json")
    template_package_version = _load_package_version(
        REPO_ROOT / "{{cookiecutter.project_slug}}" / "package.json"
    )
    pyproject_version = _load_pyproject_version(REPO_ROOT / "pyproject.toml")

    assert (
        root_package_version == EXPECTED_VERSION
    ), f"Root package.json version {root_package_version} != {EXPECTED_VERSION}"
    assert (
        template_package_version == EXPECTED_VERSION
    ), f"Template package.json version {template_package_version} != {EXPECTED_VERSION}"
    assert (
        pyproject_version == EXPECTED_VERSION
    ), f"pyproject.toml version {pyproject_version} != {EXPECTED_VERSION}"
