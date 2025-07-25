
import typer
import pandas as pd
from python.cache import put_in_cache



def birth(file_path: str = "", header: bool = True):
    """
    Charge le dataset dans le cache
    """
    try:
        df = pd.read_csv(file_path)
        typer.echo(f"📂 Dataset chargé avec succès : {len(df)} lignes dans '{file_path}'")
        answer = put_in_cache(df)
        if not answer:
            return "Impossible de mettre le dataset dans le cache"
        typer.echo("✅ Dataset sauvegardé dans le cache.")
        if header:
            typer.echo(f"📝 En-têtes : {', '.join(df.columns)}")
            typer.echo(f"📊 Aperçu des données :\n{df.head()}")
    except Exception as e:
        typer.echo(f"❌ Erreur lors du chargement du fichier : {e}")
        raise typer.Exit(code=1)
