import pandas as pd

def load_jumia_data(file_path):
    # Charger le fichier Excel avec un chemin relatif
    df = pd.read_excel(file_path)
    
    # Nettoyer la colonne 'Prix'
    df['Prix'] = df['Prix'].replace(r'[^\d.]', '', regex=True).astype(float)
    
    return df


