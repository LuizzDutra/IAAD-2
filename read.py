import streamlit as st
import controller

def get_all_tables():
    for t in controller.get_tables():
        st.write(t[1])
        st.table(t[0])

def get_table(table_name):
    if table_name == "--":
        get_all_tables()
    else:
        st.write(table_name)
        st.table(controller.get_table(table_name))

def get_read_page():
    select = st.selectbox("Tabela:", options=["--"] + controller.get_tables_names())
    get_table(select)

