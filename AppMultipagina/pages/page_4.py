import streamlit as st
import altair as alt
import pandas as pd

st.subheader("Histograma de frecuencias")
df = pd.read_csv("AppMultipagina/Datos/quality_life_2020.csv", sep=";")

# Agregar un selector de enteros para elegir el número de bines
num_bins = st.sidebar.slider("Selecciona el número de bines:", min_value=5, max_value=15, value=8, step=1)

histogram = alt.Chart(df).mark_bar().encode(
    x=alt.X('Quality of Life Index', bin=alt.Bin(maxbins=num_bins)),
    y='count()',
    tooltip='count()'
).properties(
    width=600,
    height=400
)

st.altair_chart(histogram, use_container_width=True)

st.page_link("pages/page_3.py", label="⬅️ Regresar")
st.page_link("pages/page_5.py", label="Siguiente ➡️")
