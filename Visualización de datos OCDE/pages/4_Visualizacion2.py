import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("Visualización_de_datos_OCDE/Datos/OECD.HEALTH_STATUS.csv")
    return df

df = load_data()

st.title("📈 Series de Tiempo")

# países miembros de la OCDE
ocde_paises = [
    "AUS", "AUT", "BEL", "CAN", "CHL", "CZE", "DNK", "EST", 
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", 
    "JPN", "MEX", "NLD", "NZL", "NOR", "POL", "PRT", "SVK", 
    "SVN", "ESP", "SWE", "CHE", "GBR", "USA"
]

paises_disponibles = sorted(df["REF_AREA"].unique())
paises_seleccionados = st.multiselect("Selecciona países:", paises_disponibles, default=[paises_disponibles[0]])
genero = st.radio("Seleccionar datos por género:", ["Total", "Male", "Female"])

df_filtrado = df[(df["REF_AREA"].isin(paises_seleccionados)) & (df["Sex"] == genero if genero != "Total" else True)]

# Grafica
fig, ax = plt.subplots(figsize=(10, 6))
for pais in paises_seleccionados:
    datos_pais = df_filtrado[df_filtrado["REF_AREA"] == pais]
    ax.plot(datos_pais["TIME_PERIOD"], datos_pais["OBS_VALUE"], label=pais)

ax.set_xlabel("Año")
ax.set_ylabel("Esperanza de vida")
ax.legend()
st.pyplot(fig)
