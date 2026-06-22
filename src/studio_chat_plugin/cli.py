"""Command-line entry point for the studio chat plugin."""

from studio_chat_plugin import __version__


def main() -> None:
    """Print the plugin version.

    Serves as the placeholder console-script entry point; returns
    nothing and writes the current package version to stdout.
    """
    print(f"studio-chat-plugin {__version__}")
