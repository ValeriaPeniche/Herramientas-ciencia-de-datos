import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("data/OECD.HEALTH_STATUS.csv")
    return df

df = load_data()

st.title("📊 Comparación de Distribuciones")

# Selector de año
años_disponibles = sorted(df["TIME_PERIOD"].unique(), reverse=True)
año_seleccionado = st.radio("Selecciona un año:", años_disponibles, index=0)

# Selector de comparación
opcion = st.selectbox("Comparar por:", ["Género", "Membresía OCDE"])

df_filtrado = df[df["TIME_PERIOD"] == año_seleccionado]

# Gráfica
fig, ax = plt.subplots(figsize=(8, 6))
if opcion == "Género":
    sns.boxplot(x="SEX", y="OBS_VALUE", data=df_filtrado, ax=ax)
else:
    sns.boxplot(x="REF_AREA", y="OBS_VALUE", data=df_filtrado, ax=ax)

st.pyplot(fig)
