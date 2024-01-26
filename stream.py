import streamlit as st
import pandas as pd

st.write("""
#Application de données
""")

file = st.file_uploader("charger un fichier")

a = st.button("creer une graphe", on_click="") 
b = st.button("creer un dashbord", on_click="a")
if a:
    df = pd.read_csv(str(file))
    st.altair_chart(df)

if b:
    df = pd.read_csv(file)
    st.altair_chart(df)
    st.line_chart(df)
    st.area_chart(df)
    st.bar_chart(df)
