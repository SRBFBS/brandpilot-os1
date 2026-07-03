import typer

app = typer.Typer(
    help="BrandPilot OS - Installer und Verwaltung"
)


@app.command()
def version():
    """Zeigt die aktuelle Version."""
    print("BrandPilot OS Version 0.1.0")


@app.command()
def hello():
    """Testkommando."""
    print("Hallo Sven 👋")
