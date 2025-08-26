import os
import subprocess
from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException

def test_bake_project_with_defaults(cookies):
    """
    Test that the project can be baked with default values.
    """
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-hexagon-app"
    assert result.project_path.is_dir()

    # Check for some key files
    assert (result.project_path / "package.json").is_file()
    assert (result.project_path / "docs/README.md").is_file()
    assert (result.project_path / "techstack.yaml").is_file()


def test_bake_project_with_custom_context(cookies):
    """
    Test that the project can be baked with custom context.
    """
    context = {
        "project_slug": "my-awesome-project",
        "author_name": "Test Author",
        "python_version": "3.12",
        "description": "A truly awesome project.",
    }
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-awesome-project"
    assert result.project_path.is_dir()

    # The description is not used in any generated file, so we don't check for it.


@pytest.mark.parametrize(
    "slug,is_valid",
    [
        ("invalid slug", False),
        ("Invalid-Slug", False),
        ("good-slug", True),
    ],
)
def test_pre_generation_hook_validation(cookies, slug, is_valid):
    """
    Test the pre-generation hook validation logic.
    """
    if is_valid:
        result = cookies.bake(extra_context={"project_slug": slug})
        assert result.exit_code == 0
    else:
        result = cookies.bake(extra_context={"project_slug": slug})
        assert result.exit_code != 0
        assert isinstance(result.exception, FailedHookException)


def test_generated_project_installs_and_tests_pass(cookies):
    """
    Generate the project and run its own test suite.
    This is a critical integration test.
    """
    result = cookies.bake()
    assert result.exit_code == 0
    project_path = result.project_path

    # The generated project uses pnpm, so we need to install dependencies.
    # We also need to enable corepack first.
    try:
        # Enable corepack to use pnpm
        subprocess.run(
            ["corepack", "enable"],
            check=True,
            capture_output=True,
            text=True,
        )
        # Install dependencies
        subprocess.run(
            ["pnpm", "install"],
            cwd=project_path,
            check=True,
            capture_output=True,
            text=True,
        )
        # Run the node tests
        test_result = subprocess.run(
            ["pnpm", "test:node"],
            cwd=project_path,
            check=True,
            capture_output=True,
            text=True,
        )
        logger.info("pnpm test:node stdout:")
        logger.info(test_result.stdout)
        logger.info("pnpm test:node stderr:")
        logger.info(test_result.stderr)

    except FileNotFoundError as e:
        pytest.fail(f"Command not found: {e}. Is pnpm installed and in the PATH?")
    except subprocess.CalledProcessError as e:
        logger.error("STDOUT: %s", e.stdout)
        logger.error("STDERR: %s", e.stderr)
        pytest.fail(f"Command '{' '.join(e.cmd)}' failed with exit code {e.returncode}")
