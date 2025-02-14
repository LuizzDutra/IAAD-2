import streamlit as st
import sqlalchemy as db
from sqlalchemy.dialects import mysql
from urllib.parse import quote
import pandas

st.set_page_config(
    page_title="IAAD-Equipe2",
    layout="centered"
)
st.header("IAAD Equipe 2")


#Conecta ao mysql e cria o db, dando drop caso necessário
engine = db.create_engine(f"mysql+mysqlconnector://{st.secrets['user']}:{quote(st.secrets['password'])}@{st.secrets['host']}:{st.secrets['port']}")

with open("database/schema_normalizado.sql", "r", encoding="utf-8") as file:
        script = file.read()

with engine.connect() as conn:
    statements = [stmt.strip() for stmt in script.split(';') if stmt.strip()]
    for stmt in statements:
        conn.execute(db.text(stmt))
    conn.commit()

st.write("Databases")
st.write(db.inspect(engine).get_schema_names())

with engine.connect() as conn:
    st.write("Tables")
    st.table(conn.execute(db.text("SHOW TABLES")).fetchall())
    st.write("Programadores")
    st.table(conn.execute(db.text("SELECT * FROM Programador")).fetchall())
