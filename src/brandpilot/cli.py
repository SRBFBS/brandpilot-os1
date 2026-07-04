import typer
from brandpilot.api.baserow import BaserowClient
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

@app.command()
def connect():
    """Testet die Verbindung zu Baserow."""

    client = BaserowClient()

    ok, result = client.test_connection()

    if ok:
        typer.secho("✅ Verbindung erfolgreich", fg=typer.colors.GREEN)
    else:
        typer.secho("❌ Verbindung fehlgeschlagen", fg=typer.colors.RED)
        print(result)