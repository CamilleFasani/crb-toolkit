"""Tests de la commande `crb`."""

from typer.testing import CliRunner

from crb_toolkit import __version__
from crb_toolkit.cli import app

runner = CliRunner()


def test_version_prints_number() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_help_lists_three_subcommands() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    for subcommand in ("p2p", "p2c", "p2t"):
        assert subcommand in result.output
