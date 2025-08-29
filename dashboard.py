# dashboard.py
import streamlit as st
from data_loader import load_jumia_data

# Charger les données
file_path = r"C:\Users\Galaxy\Downloads\jumia_produits (1).xlsx"
df = load_jumia_data(file_path)

# Titre
st.title("Dashboard Jumia Produits Interactif")

# 1️⃣ Menu déroulant pour choisir le produit
produit_unique = df['Produit'].unique()
selected_produit = st.selectbox("Choisir un produit :", produit_unique)

# Filtrer le DataFrame selon le produit choisi
df_filtered = df[df['Produit'] == selected_produit]

# 2️⃣ Bouton pour afficher le tableau filtré
if st.button("Afficher le tableau du produit"):
    st.subheader(f"Données pour : {selected_produit}")
    st.write(df_filtered)

# 3️⃣ Bouton pour afficher un graphique des prix par catégorie
if st.button("Afficher graphique des prix par catégorie"):
    st.subheader(f"Prix moyen par catégorie pour {selected_produit}")
    st.bar_chart(df_filtered.groupby('Catégorie')['Prix'].mean())

# 4️⃣ Checkbox pour afficher le prix moyen
if st.checkbox("Afficher le prix moyen du produit"):
    avg_price = df_filtered['Prix'].mean()
    st.write(f"Prix moyen : {avg_price:.2f} DH")

