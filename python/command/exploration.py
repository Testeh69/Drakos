import typer
from python.cache import Cache
import pandas as pd
import os






class Exploration:


    @staticmethod
    def inspect( arg = "head", number: int = 5):
        """
        Charge le dataset du cache et affiche les informations
        """
        try:
            df = Cache.load_from_cache()
            typer.echo(f"📂 Dataset chargé avec succès : {len(df)} lignes")
            if arg == "head":
                typer.echo(f"{df.head(number)}")
            elif arg == "tail":
                typer.echo(f"{df.tail(number)}")
        except Exception as e:
            typer.echo(f"❌ Erreur lors du chargement du cache : {e}")





