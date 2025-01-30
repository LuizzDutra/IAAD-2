import streamlit as st
import mysql.connector

st.set_page_config(
    page_title="IAAD-Equipe2",
    layout="centered"
)
st.header("Hello, world!")

my_db = mysql.connector.connect(
    host=st.secrets["host"],
    port=st.secrets["port"],
    user=st.secrets["user"],
    password=st.secrets["password"]
)

cursor = my_db.cursor()


cursor.execute("SHOW DATABASES")

for i in cursor:
    st.text(i)

