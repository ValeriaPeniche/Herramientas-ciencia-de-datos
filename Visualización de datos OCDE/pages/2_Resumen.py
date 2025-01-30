import streamlit as st
import pandas as pd

# Países miembros de la OCDE
ocde_paises = [
    "AUS", "AUT", "BEL", "CAN", "CHL", "CZE", "DNK", "EST", 
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", 
    "JPN", "MEX", "NLD", "NZL", "NOR", "POL", "PRT", "SVK", 
    "SVN", "ESP", "SWE", "CHE", "GBR", "USA"
]

@st.cache_data
def load_data():
    df = pd.read_csv("Visualización_de_datos_OCDE/Datos/OECD.HEALTH_STATUS.csv")
    return df

df = load_data()

años_disponibles = sorted(df["TIME_PERIOD"].unique(), reverse=True)
año_seleccionado = st.radio("Selecciona un año:", años_disponibles, index=0)

# Filtrar datos por año
df_filtrado = df[df["TIME_PERIOD"] == año_seleccionado]

# Filtrar países miembros de la OCDE 
df_ocde = df_filtrado[df_filtrado["REF_AREA"].isin(ocde_paises)]
df_no_ocde = df_filtrado[~df_filtrado["REF_AREA"].isin(ocde_paises)]

# Calcular estadísticas agrupadas
promedio_ocde = df_ocde["OBS_VALUE"].mean()
desviacion_ocde = df_ocde["OBS_VALUE"].std()
minimo_ocde = df_ocde["OBS_VALUE"].min()
maximo_ocde = df_ocde["OBS_VALUE"].max()

promedio_no_ocde = df_no_ocde["OBS_VALUE"].mean()
desviacion_no_ocde = df_no_ocde["OBS_VALUE"].std()
minimo_no_ocde = df_no_ocde["OBS_VALUE"].min()
maximo_no_ocde = df_no_ocde["OBS_VALUE"].max()

st.title("📊 Resumen Estadístico")
# Selector para ver OCDE o no
grupo_ocde = st.checkbox("Desagrupar por OCDE (Miembros vs No Miembros)")

if grupo_ocde:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Promedio (OCDE)", f"{promedio_ocde:.2f} años")
    col2.metric("Desviación Estándar (OCDE)", f"{desviacion_ocde:.2f}")
    col3.metric("Mínimo (OCDE)", f"{minimo_ocde:.2f}")
    col4.metric("Máximo (OCDE)", f"{maximo_ocde:.2f}")

    col5, col6, col7, col8 = st.columns(4)
    col5.metric("Promedio (No OCDE)", f"{promedio_no_ocde:.2f} años")
    col6.metric("Desviación Estándar (No OCDE)", f"{desviacion_no_ocde:.2f}")
    col7.metric("Mínimo (No OCDE)", f"{minimo_no_ocde:.2f}")
    col8.metric("Máximo (No OCDE)", f"{maximo_no_ocde:.2f}")
else:
    # Calcular métricas generales
    promedio_total = df_filtrado["OBS_VALUE"].mean()
    desviacion_total = df_filtrado["OBS_VALUE"].std()
    minimo_total = df_filtrado["OBS_VALUE"].min()
    maximo_total = df_filtrado["OBS_VALUE"].max()

    # Mostrar métricas sin desagrupar
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Promedio", f"{promedio_total:.2f} años")
    col2.metric("Desviación Estándar", f"{desviacion_total:.2f}")
    col3.metric("Mínimo", f"{minimo_total:.2f}")
    col4.metric("Máximo", f"{maximo_total:.2f}")
