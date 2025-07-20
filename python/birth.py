
import typer
import pandas as pd


def birth(file_path: str = "", header: bool = True):
    try:
        df = pd.read_csv(file_path)
        typer.echo(f"📂 Dataset chargé avec succès : {len(df)} lignes dans '{file_path}'")
        if header:
            typer.echo(f"📝 En-têtes : {', '.join(df.columns)}")
            typer.echo(f"📊 Aperçu des données :\n{df.head()}")
    except Exception as e:
        typer.echo(f"❌ Erreur lors du chargement du fichier : {e}")
        raise typer.Exit(code=1)
