import streamlit as st
from data_loader import load_jumia_data

# Utiliser un chemin relatif
file_path = "jumia_produits (1).xlsx"
df = load_jumia_data(file_path)

# Titre
st.title("Dashboard Jumia Produits Interactif")

# Menu déroulant pour choisir un produit
produit_unique = df['Produit'].unique()
selected_produit = st.selectbox("Choisir un produit :", produit_unique)

# Filtrer le DataFrame selon le produit choisi
df_filtered = df[df['Produit'] == selected_produit]

# Bouton pour afficher le tableau filtré
if st.button("Afficher le tableau du produit"):
    st.write(df_filtered)

# Bouton pour afficher le graphique des prix par catégorie
if st.button("Afficher graphique des prix par catégorie"):
    st.bar_chart(df_filtered.groupby('Catégorie')['Prix'].mean())

# Checkbox pour afficher le prix moyen
if st.checkbox("Afficher le prix moyen du produit"):
    avg_price = df_filtered['Prix'].mean()
    st.write(f"Prix moyen : {avg_price:.2f} DH")



