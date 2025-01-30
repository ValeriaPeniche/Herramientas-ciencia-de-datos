import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("Visualización_de_datos_OCDE/Datos/OECD.HEALTH_STATUS.csv")
    return df

df = load_data()
st.title("📊 Comparación de Distribuciones")

# Año
años_disponibles = sorted(df["TIME_PERIOD"].unique(), reverse=True)
año_seleccionado = st.radio("Selecciona un año:", años_disponibles, index=0)
# comparación
opcion = st.selectbox("Comparar por:", ["Género", "Membresía OCDE"])
# Filtrar datos
df_filtrado = df[df["TIME_PERIOD"] == año_seleccionado]

# Países miembros de la OCDE 
ocde_paises = [
    "AUS", "AUT", "BEL", "CAN", "CHL", "CZE", "DNK", "EST", 
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", 
    "JPN", "MEX", "NLD", "NZL", "NOR", "POL", "PRT", "SVK", 
    "SVN", "ESP", "SWE", "CHE", "GBR", "USA"
]
df_ocde = df_filtrado[df_filtrado["REF_AREA"].isin(ocde_paises)]
df_no_ocde = df_filtrado[~df_filtrado["REF_AREA"].isin(ocde_paises)]

# Gráfica
fig, ax = plt.subplots(figsize=(8, 6))

if opcion == "Género":
    sns.boxplot(x="SEX", y="OBS_VALUE", data=df_filtrado, ax=ax)
else:
    df_filtrado["Membresía OCDE"] = df_filtrado["REF_AREA"].apply(
        lambda x: "Miembro OCDE" if x in ocde_paises else "No Miembro OCDE"
    )
    sns.boxplot(x="Membresía OCDE", y="OBS_VALUE", data=df_filtrado, ax=ax)
st.pyplot(fig)
