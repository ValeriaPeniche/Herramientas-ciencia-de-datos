import streamlit as st

# Navegación con st.navigation
pg = st.navigation([
    st.Page("pages/page_1.py", title="Inicio"),
    st.Page("pages/page_2.py", title="Tabla de datos"),
    st.Page("pages/page_3.py", title="Gráfica de barras"),
    st.Page("pages/page_4.py", title="Histograma"),
    st.Page("pages/page_5.py", title="Gráfica de caja"),
    st.Page("pages/page_6.py", title="Gráfica de dispersión"),
])
# Ejecutar página
pg.run()
