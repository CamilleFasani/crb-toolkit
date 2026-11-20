"""Point d'entrée de la commande `crb` et de ses sous-commandes."""

import typer

from crb_toolkit import __version__

app = typer.Typer(
    help="crb-toolkit — A toolkit for capturing the beauty of reality – at least trying to.",
    no_args_is_help=True,
)


def show_version(value: bool) -> None:
    """Affiche la version puis quitte, si l'option --version est donnée."""
    if value:
        typer.echo(f"crb-toolkit {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        callback=show_version,
        is_eager=True,
        help="Affiche la version et quitte.",
    ),
) -> None:
    """Options communes à toutes les sous-commandes."""


@app.command("p2p")
def p2p() -> None:
    """P2P - From Photo to Palette : extrait une palette d'une photo."""
    typer.echo("P2P : pas encore implémenté.")
    raise typer.Exit(code=1)


@app.command("p2c")
def p2c() -> None:
    """P2C - From Palette to Canvas : crée un tableau impressionniste."""
    typer.echo("P2C : pas encore implémenté.")
    raise typer.Exit(code=1)


@app.command("p2t")
def p2t() -> None:
    """P2T - From Photo to Texture : extrait une texture d'une photo."""
    typer.echo("P2T : pas encore implémenté.")
    raise typer.Exit(code=1)
