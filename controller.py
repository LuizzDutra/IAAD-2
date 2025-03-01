import streamlit as st
import sqlalchemy as db
from sqlalchemy.dialects import mysql
from urllib.parse import quote
import sqlparse


#Conecta ao mysql e cria o db, dando drop caso necessário
engine = db.create_engine(f"mysql+mysqlconnector://{st.secrets['user']}:{quote(st.secrets['password'])}@{st.secrets['host']}:{st.secrets['port']}")
with engine.connect() as conn:
    conn.execute(db.text("USE db_equipe2"))

def create_schema():
    with open("database/schema_normalizado.sql", "r", encoding="utf-8") as file:
            script = file.read()

    with engine.connect() as conn:
        #statements = [stmt.strip() for stmt in script.split(';') if stmt.strip()]
        statements = sqlparse.split(script)
        st.write(statements)
        for stmt in statements:
            conn.execute(db.text(stmt))
        conn.commit()


def get_schemas():
    return db.inspect(engine).get_schema_names()

def get_tables_names():
    with engine.connect() as conn:
        #conn.execute(db.text("USE db_equipe2"))
        query = conn.execute(db.text("SHOW FULL TABLES WHERE TABLE_TYPE = 'BASE TABLE'")).fetchall()
        return [t[0] for t in query]

def get_tables() -> dict:
    tables = get_tables_names()
    return {t : get_table(t) for t in tables}

def get_table(table_name):
    with engine.connect() as conn:
        return conn.execute(db.text(f"SELECT * FROM {table_name}")).fetchall()
    
def get_table_columns(table_name):
    with engine.connect() as conn:
        return conn.execute(db.text(f"SELECT * FROM {table_name}")).keys()


def get_views_names():
    with engine.connect() as conn:
        #conn.execute(db.text("USE db_equipe2"))
        query = conn.execute(db.text("SHOW FULL TABLES WHERE TABLE_TYPE = 'VIEW'")).fetchall()
        return [t[0] for t in query]


def make_query(query: str):
    with engine.connect() as conn:
        conn.execute(db.text("USE db_equipe2"))
        ret = conn.execute(db.text(query))
        conn.commit()
    return ret


def update_query(table_name, primary_key, primary_value, updates):
    if not updates:
        return "Nenhuma alteração feita."

    # Monta a query dinamicamente
    update_query = f"UPDATE {table_name} SET "
    update_query += ", ".join([f"{col} = :{col}" for col in updates.keys()])
    update_query += f" WHERE {primary_key} = :primary_value"

    try:
        with engine.connect() as conn:
            conn.execute(db.text(update_query), {"primary_value": primary_value, **updates})
            conn.commit()
        return "Registro atualizado com sucesso!"
    except Exception as e:
        return f"Erro ao atualizar o registro: {e}"

    