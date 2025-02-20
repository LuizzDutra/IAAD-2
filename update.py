from controller import update_query, get_tables_names, get_table_columns
import streamlit as st
import controller

def get_update_page():
    # Exemplo de interface para atualizar registros
    st.subheader("Atualizar Programador")

    # Pega as tabelas e colunas do banco
    tables = controller.get_tables_names()
    table_to_update = st.selectbox("Escolha a tabela", tables)

    if table_to_update:
        columns = list(controller.get_table_columns(table_to_update))  
        st.write("Colunas:", columns)

        # Selecione a chave primária
        primary_key = columns[0]  

        primary_value = st.text_input(f"Valor para {primary_key}")  

        if primary_value:
            updates = {}
            for col in columns:
                if col != primary_key:  
                    value = st.text_input(f"Novo valor para {col}")
                    if value:
                        updates[col] = value

            # Botão de atualização
            if st.button("Atualizar"):
                if updates:  
                    result = controller.update_query(table_to_update, primary_key, primary_value, updates)
                    st.write(result)
                else:
                    st.warning("Nenhum campo para atualizar foi selecionado.")