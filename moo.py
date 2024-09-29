import streamlit as st
import os
import sys

st.title("Moo Site")
st.write("Bienvenue sur le site officel de SuperMoo !")
 # URL de l'image
image_url = "https://cdn.discordapp.com/attachments/1280051118872985703/1289896394206744586/image.png?ex=66fa7d21&is=66f92ba1&hm=f97a1911ac49d9994468a06a6a49ef408f2bc62a4e9e4976ac61e9718a1bca88&"
    
# Afficher l'image depuis l'URL sans légende ni colonne de largeur ajustée
st.image(image_url)
st.write("Ca c'est les moutons et poules de Lego Fortnite.")
st.write("Perso, je trouve ça dingue ils ont des noms comme ça...")