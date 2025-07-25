
import typer
import pandas as pd
from python.cache import Cache
import json
import os

class Vault:


    @staticmethod
    def lair(config_path:str = "drk_stgs/config.json"):
        """
        create the config file with the path of the project put in
        drk_stgs stand for Drakos Settings

        """
        if not os.path.exists("drk_stgs"):
            os.makedirs("drk_stgs")
            typer.echo("📂 Dossier 'drk_stgs' créé pour les configurations.")
        config_data = {"path": os.getcwd()}
        with open(config_path, mode = "w", encoding = "utf-8") as file:
            json.dump(config_data, file, indent=4 )
        typer.echo(f"📁 Lair configuré dans : {config_path}")


    @staticmethod
    def detect_lair():
        """
        Vérifie si le fichier de configuration existe
        """
        actual_path = os.getcwd()
        path = os.path.join(actual_path, "drk_stgs/config.json")
        answer = os.path.exists(path)
        typer.echo(f"🔍 Vérification du lair : {'Trouvé' if answer else 'Non trouvé'}")
        return answer

        

    @staticmethod
    def birth(name_file: str = "", header: bool = True):
        """
        Charge le dataset dans le cache
        """
        verification = Vault.detect_lair()
        if verification and name_file != "":

            file_path = os.path.join(os.getcwd(), name_file)
            try:
                df = pd.read_csv(file_path)
                typer.echo(f"📂 Dataset chargé avec succès : {len(df)} lignes dans '{file_path}'")
                answer = Cache.put_in_cache(df)
                if not answer:
                    return "Impossible de mettre le dataset dans le cache"
                typer.echo("✅ Dataset sauvegardé dans le cache.")
                if header:
                    typer.echo(f"📝 En-têtes : {', '.join(df.columns)}")
                    typer.echo(f"📊 Aperçu des données :\n{df.head()}")
            except Exception as e:
                typer.echo(f"❌ Erreur lors du chargement du fichier : {e}")
                raise typer.Exit(code=1)
            
        else:
            if not verification:
                typer.echo(f"❌ Aucun fichier de configuration détecté. Veuillez créer un lair avec 'drk vault lair'.")
            else:
                typer.echo(f"❌ Le nom du fichier est vide ou incorrect : {name_file}")
