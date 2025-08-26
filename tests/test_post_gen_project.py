from unittest.mock import patch

# It's a bit tricky to import a script that's not in a package,
# so we'll just read the file and exec it.
with open("hooks/post_gen_project.py") as f:
    POST_GEN_SCRIPT = f.read()


def run_post_gen_script(slug):
    """Helper to run the post-gen script with patched globals."""
    # The script uses `{{ ... }}` syntax, which is not valid Python.
    # We need to replace these with the actual values.
    script = POST_GEN_SCRIPT.replace(
        '{{ cookiecutter.project_slug }}', slug
    )

    with patch("builtins.print") as mock_print:
        exec(script, globals())
        return mock_print


def test_post_gen_script_runs():
    """Test that the post-gen script runs without errors."""
    mock_print = run_post_gen_script("my-test-project")
    mock_print.assert_called()
    # Check that some expected output is present
    assert any("Generation complete!" in call.args[0] for call in mock_print.call_args_list)
