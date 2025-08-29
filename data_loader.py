import pandas as pd

def load_jumia_data(file_path):
    """
    Charge et nettoie le fichier Excel Jumia.

    Paramètre :
        file_path (str) : chemin vers le fichier Excel

    Retour :
        pd.DataFrame : DataFrame prêt pour visualisation
    """
    # Charger le fichier Excel
    df = pd.read_excel(file_path)

    # Afficher quelques infos (optionnel)
    print(df.head())
    print(df.info())
    print(df.describe())

    # Nettoyer la colonne Prix
    df['Prix'] = df['Prix'].replace(r'[^\d.]', '', regex=True).astype(float)

    # Vérification après nettoyage
    print(df.info())
    print(df.head())

    # Retourner le DataFrame
    return df

# Test rapide si on exécute directement ce fichier
if __name__ == "__main__":
    file_path = r"C:\Users\Galaxy\Downloads\jumia_produits (1).xlsx"
    df = load_jumia_data(file_path)
