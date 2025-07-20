import typer
import pandas as pd
from sklearn.preprocessing import LabelEncoder



def glyph(file_path: str = typer.Argument(..., help="Chemin du dataset CSV"),
          save_path: str = typer.Option("", help="Chemin pour sauvegarder le dataset transformé"),
          columns: list[str] = typer.Option([], help="Liste des colonnes à encoder (si vide, toutes les colonnes object)")):
    try:
        df = pd.read_csv(file_path)
        if not columns:
            columns = df.select_dtypes(include=['object']).columns.tolist()
        
        le = LabelEncoder()
        for col in columns:
            df[col] = le.fit_transform(df[col].astype(str))
            typer.echo(f"✅ Colonne '{col}' encodée en numérique.")

        if save_path:
            df.to_csv(save_path, index=False)
            typer.echo(f"💾 Dataset sauvegardé dans {save_path}")
        else:
            typer.echo("⚠️ Aucun chemin de sauvegarde fourni, modifications non sauvegardées.")
    except Exception as e:
        typer.echo(f"❌ Erreur pendant l'encodage : {e}")
        raise typer.Exit(code=1)
