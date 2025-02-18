import streamlit as st
import controller
import altair as alt

def get_all_tables():
    tables = controller.get_tables()
    for name, table in tables.items():
        st.write(name)
        st.table(table)

def get_table(table_name):
    if table_name == "Todas":
        get_all_tables()
    elif table_name != "Nenhuma":
        st.table(controller.get_table(table_name))

def get_all_consultas():
    views = controller.get_views_names()
    for v in views:
        st.write(v)
        st.table(controller.get_table(v))

def get_consulta(consulta: str):
    if consulta == "Todas":
        get_all_consultas()
    elif consulta != "Nenhuma":
        get_table(consulta)

def get_read_page():
    st.header("Tabelas")
    select = st.selectbox("Tabela:", options=["Nenhuma", "Todas"] + controller.get_tables_names(), label_visibility="hidden")
    get_table(select) 
    st.header("Consultas")
    select_consulta = st.selectbox("Consulta:", options=["Nenhuma", "Todas"] + controller.get_views_names(), label_visibility="hidden")
    get_consulta(select_consulta)

