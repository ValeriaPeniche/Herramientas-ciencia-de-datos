import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Importar datos
df = pd.read_csv("Datos/quality_life_2020.csv", sep=";")

# Configuración de navegación entre páginas
st.title("Calidad de vida a nivel mundial")

# Crear un menú de navegación con las páginas
menu = ["Inicio", "Tabla de datos", "Gráfica de barras", "Histograma", "Gráfica de caja", "Gráfica de dispersión"]
choice = st.navigation(menu)

# Definir el contenido de cada página
if choice == "Inicio":
    st.subheader("Indicadores")
    st.markdown("""
        En esta aplicación exploraremos la distribución de diferentes indicadores que nos permiten medir la calidad de vida en diferentes países.  
        Exploraremos los siguientes:
        * Índice de calidad de vida.
        * Índice de poder de compra.
        * Índice de seguridad.
        * Índice de salud.
        * Índice de costo de vida.
        * Razón de precios de la propiedad.
        * Índice de tiempo de desplazamiento.
        * Índice de contaminación.
        * Índice climático.
    """)
    st.page_link("Ir a Tabla de datos", target_page="Tabla de datos")

elif choice == "Tabla de datos":
    st.subheader("Tabla de datos")
    st.write("Los datos que exploraremos están disponibles en la siguiente tabla:")
    st.dataframe(df)
    st.page_link("Siguiente: Gráfica de barras", target_page="Gráfica de barras")
    st.page_link("Anterior: Inicio", target_page="Inicio")

elif choice == "Gráfica de barras":
    st.subheader("Gráfica de barras")
    order = st.radio("Ordenar por índice de calidad de vida:", ("Ascendente", "Descendente"))
    ascending = True if order == "Ascendente" else False
    # Agregar gráfico de barras aquí
    st.page_link("Siguiente: Histograma", target_page="Histograma")
    st.page_link("Anterior: Tabla de datos", target_page="Tabla de datos")

elif choice == "Histograma":
    st.subheader("Histograma de frecuencias")
    num_bins = st.slider("Selecciona el número de bines:", min_value=5, max_value=15, value=8, step=1)
    histogram = alt.Chart(df).mark_bar().encode(
        x=alt.X('Quality of Life Index', bin=alt.Bin(maxbins=num_bins)),
        y='count()',
        tooltip='count()'
    ).properties(
        width=600,
        height=400
    )
    st.altair_chart(histogram, use_container_width=True)
    st.page_link("Siguiente: Gráfica de caja", target_page="Gráfica de caja")
    st.page_link("Anterior: Gráfica de barras", target_page="Gráfica de barras")

elif choice == "Gráfica de caja":
    st.subheader("Gráfico de caja y bigotes")
    variables_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    variable_seleccionada = st.selectbox("Selecciona la variable para la gráfica de caja", variables_numericas)
    box_plot = alt.Chart(df).mark_boxplot().encode(
        y=alt.Y(f'{variable_seleccionada}:Q', scale=alt.Scale(zero=False))
    ).properties(
        width=600,
        height=400
    )
    st.altair_chart(box_plot, use_container_width=True)
    st.page_link("Siguiente: Gráfica de dispersión", target_page="Gráfica de dispersión")
    st.page_link("Anterior: Histograma", target_page="Histograma")

elif choice == "Gráfica de dispersión":
    st.subheader("Gráfica de dispersión")
    variables_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    var_1 = st.selectbox("Selecciona variable 1 (horizontal)", variables_numericas)
    var_2 = st.selectbox("Selecciona variable 2 (vertical)", variables_numericas)
    scatter_chart = alt.Chart(df).mark_circle().encode(
        x=alt.X(var_1, scale=alt.Scale(zero=False)),
        y=alt.Y(var_2, scale=alt.Scale(zero=False)),
        tooltip=['Country', var_1, var_2]
    )
    st.altair_chart(scatter_chart, use_container_width=True)
    st.write(f'Correlación entre {var_1} y {var_2}: {np.round(df[var_1].corr(df[var_2]), 2)}')
    st.page_link("Anterior: Gráfica de caja", target_page="Gráfica de caja")

