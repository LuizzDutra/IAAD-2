Repositório da equipe 2 para o trabalho de IAAD.

Instruções para utilizar o repositório:

1. Crie um ambiente virtual ```python -m venv nome_do_ambiente```

2. Ative o ambiente virtual ```.\nome_do_ambiente\Scripts\activate```

3. Instale os requerimentos ```pip install -r .\requirements.txt```

4. Crie os secrets do streamlit
    1. Crie uma pasta chamada .streamlit/
    2. Adicione o arquivo secrets.toml na pasta
    3. Adicione e preencha os seguintes campos do arquivo
        ```
        host = "xxxx"
        port = xxxx
        user = "xxxx"
        password = "xxxxxxx
        ```

5. Inicie o app com ```python -m streamlit run app.py```