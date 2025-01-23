import streamlit as st
import pandas as pd

st.subheader("Tabla de datos")
st.write("Los datos que exploraremos están disponibles en la siguiente tabla:")
df = pd.read_csv("AppMultipagina/Datos/quality_life_2020.csv", sep=";")
st.dataframe(df)

st.page_link("pages/page_1.py", label="⬅️ Regresar")
st.page_link("pages/page_3.py", label="Siguiente ➡️")
