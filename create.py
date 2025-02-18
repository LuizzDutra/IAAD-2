import streamlit as st
import controller
import sqlalchemy as db
from sqlalchemy.dialects import mysql
from urllib.parse import quote

def get_create_page():
    st.header("Tabelas")
    table = st.selectbox(label= "Selecione uma tabela",options = controller.get_tables_names(),)
    data = inputs_table(table)
    if st.button(label="Enviar fomulario"):
        create_execute(data=data,table=table)
    

def inputs_table(table_name:str):
    columns = fetch_columns(table_name)
    inputs_length = len(columns)
    dict_columns = {}
    for element in columns:
        dict_columns[element] = None

    for column in columns:
        dict_columns[column] = st.text_input(label=column)
    
    return dict_columns


def fetch_columns(table_name:str):
    list = []
    query = controller.make_query(f"""
        SELECT COLUMN_NAME 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_SCHEMA = 'db_equipe2' 
        AND TABLE_NAME = '{table_name}'
    """).fetchall()

    for element in query: 
        list.append(element[0])

    return list

def create_execute(data:dict,table):
    list = []
    for key, value in data.items():
        if value == "":
            return
        if value.isdigit():
            value = int(value)
        list.append(value)
    result = tuple(i for i in list)
    try:
        #conversão da string para tirar as aspas ao usar fstring
        keyStr = ", ".join([i for i in data.keys()])
        queryStr = f"INSERT INTO {table}({keyStr}) VALUES{result}"
        st.write(queryStr)
        controller.make_query(queryStr)
    except Exception as e:
        st.text(e)
        return






    
  