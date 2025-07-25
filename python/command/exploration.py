import typer
from typer import Option
from python.cache import Cache
import pandas as pd
import os


"""
Classe pour gérer l'exploration des datasets


"""



class Exploration:


    @staticmethod
    def inspect( arg = typer.Option("head", help = "head or tail"), number: int = typer.Option(5, help = "Number of rows to display")):
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


    @staticmethod
    def first_fly():
        """
        Affiche les statistiques de base du dataset
        """
        try:
            df = Cache.load_from_cache()
            typer.echo("📊 Statistiques de base du dataset :")
            typer.echo(f"------------")
            typer.echo(f"{df.describe()}")
            typer.echo(f"------------")
            typer.echo(f"{df.info()}")
        except Exception as e:
            typer.echo(f"❌ Erreur lors de l'affichage des statistiques : {e}")



