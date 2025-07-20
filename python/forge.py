import typer
import pandas as pd
from sklearn.preprocessing import LabelEncoder
try:
    from statsmodels.imputation.mice import MICEData
    mice_available = True
except ImportError:
    mice_available = False

def forge(
    file_path: str = typer.Argument(..., help="Chemin du dataset CSV"),
    save_path: str = typer.Option(..., help="Chemin où sauvegarder le dataset modifié"),
    ops: list[str] = typer.Option(["ffill"], help="Opérations: ffill, bfill, remove, mice", show_default=True)
):
    """
    Transforme les valeurs manquantes dans le dataset en appliquant :
    - 'ffill' : forward fill
    - 'bfill' : backward fill
    - 'remove': suppression des lignes avec valeurs manquantes
    - 'mice'  : imputation multiple par chaînes (MICE)

    Le dataset modifié est sauvegardé dans save_path.
    """
    try:
        df = pd.read_csv(file_path)

        for operation in ops:
            if operation == "ffill":
                df.fillna(method='ffill', inplace=True)
                typer.echo("✅ Valeurs manquantes remplies avec 'ffill'.")
            elif operation == "bfill":
                df.fillna(method='bfill', inplace=True)
                typer.echo("✅ Valeurs manquantes remplies avec 'bfill'.")
            elif operation == "remove":
                df.dropna(inplace=True)
                typer.echo("✅ Lignes avec valeurs manquantes supprimées.")
            elif operation == "mice":
                if not mice_available:
                    typer.echo("❌ statsmodels non installé, impossible d'utiliser MICE. Faites : pip install statsmodels")
                    raise typer.Exit(code=1)
                typer.echo("🧙‍♂️ Imputation avec MICE en cours...")
                mice_data = MICEData(df)
                df_imputed = mice_data.data
                df = df_imputed  # Remplace df par la version imputée
                typer.echo("✅ Imputation MICE terminée.")
            else:
                typer.echo(f"❌ Opération '{operation}' non reconnue. Utilisez 'remove', 'ffill', 'bfill' ou 'mice'.")

        df.to_csv(save_path, index=False)
        typer.echo(f"💾 Dataset sauvegardé dans '{save_path}'")

    except Exception as e:
        typer.echo(f"❌ Erreur lors de la transformation du fichier : {e}")
        raise typer.Exit(code=1)