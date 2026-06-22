"""Tests for the CLI entry point."""

from studio_chat_plugin import __version__
from studio_chat_plugin.cli import main


def test_main_prints_version(capsys):
    """main() writes the package version to stdout."""
    main()
    captured = capsys.readouterr()
    assert __version__ in captured.out
