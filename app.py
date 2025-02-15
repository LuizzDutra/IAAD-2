import streamlit as st

import controller

st.set_page_config(
    page_title="IAAD-Equipe2",
    layout="centered"
)
st.header("IAAD Equipe 2")


controller.create_schema()

st.write("Databases")
st.write(controller.get_schemas())

st.write("Tables")
st.table(controller.get_tables())

st.write("Programadores")
st.table(controller.make_query('SELECT * FROM Programador'))

st.write("Linguagem")
st.table(controller.make_query('SELECT * FROM Linguagem'))
