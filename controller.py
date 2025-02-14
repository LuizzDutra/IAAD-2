import streamlit as st
import sqlalchemy as db
from sqlalchemy.dialects import mysql
from urllib.parse import quote


#Conecta ao mysql e cria o db, dando drop caso necessário
engine = db.create_engine(f"mysql+mysqlconnector://{st.secrets['user']}:{quote(st.secrets['password'])}@{st.secrets['host']}:{st.secrets['port']}")

def create_schema():
    with open("database/schema_normalizado.sql", "r", encoding="utf-8") as file:
            script = file.read()

    with engine.connect() as conn:
        statements = [stmt.strip() for stmt in script.split(';') if stmt.strip()]
        for stmt in statements:
            conn.execute(db.text(stmt))
        conn.commit()


def get_schemas():
    return db.inspect(engine).get_schema_names()

def get_tables():
    with engine.connect() as conn:
        return conn.execute(db.text("SHOW TABLES")).fetchall()

def get_programadores():
     with engine.connect() as conn:
        return conn.execute(db.text("SELECT * FROM Programador")).fetchall()

def make_query(query: str):
    with engine.connect() as conn:
        return conn.execute(db.text(query))
    