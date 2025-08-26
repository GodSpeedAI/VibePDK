import sys
import pytest
from unittest.mock import patch

# It's a bit tricky to import a script that's not in a package,
# so we'll just read the file and exec it.
with open("hooks/pre_gen_project.py") as f:
    PRE_GEN_SCRIPT = f.read()


def run_pre_gen_script(monkeypatch, slug, author, pyver, description):
    """Helper to run the pre-gen script with patched globals."""
    # The script uses `{{ ... }}` syntax, which is not valid Python.
    # We need to replace these with the actual values.
    # We also need to mock sys.exit.
    script = PRE_GEN_SCRIPT.replace(
        '{{ cookiecutter.project_slug }}', slug
    ).replace(
        '{{ cookiecutter.author_name }}', author
    ).replace(
        '{{ cookiecutter.python_version }}', pyver
    ).replace(
        '{{ cookiecutter.description }}', description
    )

    with patch("builtins.print") as mock_print, \
         patch("sys.exit", side_effect=ValueError("sys.exit called")) as mock_exit:
        try:
            exec(script, globals())
        except ValueError as e:
            if "sys.exit called" not in str(e):
                raise
        return mock_print, mock_exit


@pytest.mark.parametrize("slug", ["good-slug", "good_slug", "good123"])
def test_project_slug_valid(monkeypatch, slug):
    mock_print, mock_exit = run_pre_gen_script(
        monkeypatch, slug, "author", "3.11", "description"
    )
    mock_exit.assert_not_called()


@pytest.mark.parametrize("slug", ["BadSlug", "bad slug", "bad-", "-bad", "a", "a"*51])
def test_project_slug_invalid(monkeypatch, slug):
    mock_print, mock_exit = run_pre_gen_script(
        monkeypatch, slug, "author", "3.11", "description"
    )
    mock_exit.assert_called_once_with(1)


def test_author_name_valid(monkeypatch):
    mock_print, mock_exit = run_pre_gen_script(
        monkeypatch, "slug", "author", "3.11", "description"
    )
    mock_exit.assert_not_called()


def test_author_name_invalid(monkeypatch):
    mock_print, mock_exit = run_pre_gen_script(
        monkeypatch, "slug", "", "3.11", "description"
    )
    mock_exit.assert_called_once_with(1)


@pytest.mark.parametrize("pyver", ["3.10", "3.11", "3.12", "3.10.1"])
def test_python_version_valid(monkeypatch, pyver):
    mock_print, mock_exit = run_pre_gen_script(
        monkeypatch, "slug", "author", pyver, "description"
    )
    mock_exit.assert_not_called()


@pytest.mark.parametrize("pyver", ["2.7", "3.9", "3.13", "3.10a1"])
def test_python_version_invalid(monkeypatch, pyver):
    mock_print, mock_exit = run_pre_gen_script(
        monkeypatch, "slug", "author", pyver, "description"
    )
    mock_exit.assert_called_once_with(1)


def test_description_valid(monkeypatch):
    mock_print, mock_exit = run_pre_gen_script(
        monkeypatch, "slug", "author", "3.11", "long enough description"
    )
    mock_exit.assert_not_called()


def test_description_invalid(monkeypatch):
    mock_print, mock_exit = run_pre_gen_script(
        monkeypatch, "slug", "author", "3.11", "desc"
    )
    mock_exit.assert_called_once_with(1)
