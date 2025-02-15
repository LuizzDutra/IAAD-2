import streamlit as st
import controller

def get_all_tables():
    tables = controller.get_tables()
    for name, table in tables.items():
        st.write(name)
        st.table(table)

def get_table(table_name):
    if table_name == "Nenhuma":
        st.write()
    elif table_name == "Todas":
        get_all_tables()
    else:
        st.write(table_name)
        st.table(controller.get_table(table_name))


def get_consulta(consulta: str):
    st.table(controller.make_query("""SELECT NOME_STARTUP, NOME_PROGRAMADOR FROM startup NATURAL LEFT JOIN programador_startup NATURAL LEFT JOIN Programador
                                   WHERE NOME_PROGRAMADOR IS NOT NULL
                                    GROUP BY NOME_STARTUP""").fetchall())

def get_read_page():
    st.header("Tabelas")
    select = st.selectbox("", options=["Nenhuma", "Todas"] + controller.get_tables_names())
    get_table(select)
    st.header("Consultas")
    select_consulta = st.selectbox("", options=["Programadores por Startup"])
    get_consulta(select_consulta)

