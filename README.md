# Sorteador para o processo seletivo

Software utilizado para o sorteio do processo seletivo do IFS.

## Pré-requisitos

Para realizar a instalação dos pré-requisitos para executar o script, realize os seguintes passos:

1. [Instale, crie and ative um ambiente virtual](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/);
2. [Instale as dependências](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/#using-requirements-files).

## Executar

Para executar o script, realize os seguintes passos:

1. [Ative o ambiente virtual](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/);
2. Calcule ou consiga a semente;
3. Baixe a lista de inscritos;
4. Execute o seguinte comando no terminal:
    ```bash
    # A semente é um valor numérico
    # Para gerar um arquivo em CSV (para poder visualizar em ferramentas de planilha como o LibreOffice ou Excel) o terceiro argumento do script deve ser "csv"
    python main.py <semente> lista_inscritos_ordenada.csv csv resultado.csv
    # Para gerar um arquivo em HTML (para poder visualizar em um navegador como o Firefox, Chrome, Edge, entre outros) o terceiro argumento do script deve ser "html"
    python main.py <semente> lista_inscritos_ordenada.csv html resultado.html
    ```
