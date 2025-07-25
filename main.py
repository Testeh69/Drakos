import typer

from python.command.vault import Vault
from python.command.exploration import Exploration


app = typer.Typer(
    help="Drakos CLI — Outils pour manipuler et analyser des datasets CSV "
         "avec des commandes dédiées à l'inspection, l'encodage, la gestion des valeurs manquantes, etc."
)


app.command()(Vault.lair)
app.command()(Vault.detect_lair)
app.command()(Vault.birth)


app.command()(Exploration.inspect)





if __name__ == "__main__":
    app()