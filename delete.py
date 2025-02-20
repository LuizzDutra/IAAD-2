import streamlit as st
import controller
import sqlalchemy as db
from sqlalchemy.dialects import mysql
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote
from random import randint

def get_delete_page():
    st.header("Tabelas")
    table = st.selectbox(label= "Selecione uma tabela",options = controller.get_tables_names(),key = "delete_page")
    campo = input_table(table)
    if st.button(label="Enviar fomulario", key= "campo delete"):
        delete_execute(data=campo,table=table,column = fetch_column(table))
    

def input_table(table_name:str):
    column = fetch_column(table_name)
    ref = st.text_input(label=column,key= column)
    return ref
    
    


def fetch_column(table_name:str):
    columns = list(controller.get_table_columns(table_name))
    return columns[0]

def delete_execute(data:str,table,column):
    try:
        if(data == ""):
            return
        queryStr = f"DELETE FROM {table} WHERE {column} = {data};"
        st.write(queryStr)
        controller.make_query(queryStr)
    except SQLAlchemyError as e:
        st.text(e.orig)
    except Exception as e:
        st.text(e)
        return