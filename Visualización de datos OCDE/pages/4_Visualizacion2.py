import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("data/OECD.HEALTH_STATUS.csv")
    return df

df = load_data()

st.title("📈 Series de Tiempo")

# Selector de países
paises_disponibles = sorted(df["REF_AREA"].unique())
paises_seleccionados = st.multiselect("Selecciona países:", paises_disponibles, default=[paises_disponibles[0]])

# Selector de género
genero = st.radio("Seleccionar datos por género:", ["Total", "Males", "Females"])

# Filtrar datos
df_filtrado = df[(df["REF_AREA"].isin(paises_seleccionados)) & (df["SEX"] == genero)]

# Graficar
fig, ax = plt.subplots(figsize=(10, 6))
for pais in paises_seleccionados:
    datos_pais = df_filtrado[df_filtrado["REF_AREA"] == pais]
    ax.plot(datos_pais["TIME_PERIOD"], datos_pais["OBS_VALUE"], label=pais)

ax.set_xlabel("Año")
ax.set_ylabel("Esperanza de vida")
ax.legend()
st.pyplot(fig)
