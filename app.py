import streamlit as st
import read
import create
import delete
import controller

st.set_page_config(
    page_title="IAAD-Equipe2",
    layout="centered"
)
st.header("IAAD Equipe 2")

main_tab, create_tab, delete_tab, read_tab,  = st.tabs(["Main", "Create","Delete","Read"])

@st.cache_data
def init_schema():
    controller.create_schema()


with main_tab:
    st.write("Databases")
    st.write(controller.get_schemas())

    st.write("Tables")
    st.table(controller.get_tables_names())

    if st.button("Resetar schema"):
        init_schema.clear()
        init_schema()


with create_tab:
    create.get_create_page()

with delete_tab:
    delete.get_delete_page()

with read_tab:
    read.get_read_page()
