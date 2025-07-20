import typer
import pandas as pd




def inspect(file_path: str = "", hasnulls: bool = False):
    try:
        df = pd.read_csv(file_path)
        typer.echo(f"📂 Informations sur le dataset '{file_path}':")
        typer.echo(f"📊 Nombre de lignes : {len(df)}")
        typer.echo(f"📈 Types de données :\n{df.dtypes}")
        typer.echo(f"📊 Description des valeurs{df.describe()}")
        if hasnulls:
            null_counts = df.isnull().sum()
            null_columns = null_counts[null_counts > 0]
            if not null_columns.empty:
                typer.echo(f"⚠️ Colonnes avec des valeurs manquantes :\n{null_columns}")
            else:
                typer.echo("✅ Aucune valeur manquante dans le dataset.")
    except Exception as e:
        typer.echo(f"❌ Erreur lors de l'inspection du fichier : {e}")
        raise typer.Exit(code=1)