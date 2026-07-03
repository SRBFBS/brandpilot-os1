import typer

app = typer.Typer(help="BrandPilot OS")


@app.callback()
def main():
    """
    BrandPilot OS
    """
    pass


@app.command()
def doctor():
    """Prüft die Entwicklungsumgebung."""
    typer.echo("🧯 BrandPilot OS")
    typer.echo("✅ CLI funktioniert!")