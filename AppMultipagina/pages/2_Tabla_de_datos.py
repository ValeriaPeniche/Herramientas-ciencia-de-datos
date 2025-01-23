import streamlit as st
import pandas as pd

st.subheader("Tabla de datos")
st.write("Los datos que exploraremos están disponibles en la siguiente tabla:")
df = pd.read_csv("Datos/quality_life_2020.csv", sep=";")
st.dataframe(df)

st.page_link("pages/1_Indicadores_calidad_de_vida.py", label="⬅️ Regresar a Inicio")
st.page_link("pages/3_Grafica_de_barras.py", label="Siguiente ➡️")
