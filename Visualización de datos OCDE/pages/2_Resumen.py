import streamlit as st
import pandas as pd

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("Datos/OECD.HEALTH_STATUS.csv")
    return df

df = load_data()

st.title("📊 Resumen Estadístico")

# Selector de año
años_disponibles = sorted(df["TIME_PERIOD"].unique(), reverse=True)
año_seleccionado = st.radio("Selecciona un año:", años_disponibles, index=0)

# Filtrar datos por año seleccionado
df_filtrado = df[df["TIME_PERIOD"] == año_seleccionado]

# Calcular métricas
promedio = df_filtrado["OBS_VALUE"].mean()
desviacion = df_filtrado["OBS_VALUE"].std()
minimo = df_filtrado["OBS_VALUE"].min()
maximo = df_filtrado["OBS_VALUE"].max()

# Mostrar métricas en tarjetas
col1, col2, col3, col4 = st.columns(4)
col1.metric("Promedio", f"{promedio:.2f} años")
col2.metric("Desviación Estándar", f"{desviacion:.2f}")
col3.metric("Mínimo", f"{minimo:.2f}")
col4.metric("Máximo", f"{maximo:.2f}")
