import typer

from python.birth import birth
from python.inspect import inspect
from python.glyph import glyph
from python.forge import forge

app = typer.Typer(
    help="Drakos CLI — Outils pour manipuler et analyser des datasets CSV "
         "avec des commandes dédiées à l'inspection, l'encodage, la gestion des valeurs manquantes, etc."
)

app.command()(birth)
app.command()(inspect)
app.command()(glyph)
app.command()(forge)

if __name__ == "__main__":
    app()