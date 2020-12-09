import csv

def carregar_lista(caminho_arquivo):
    lista = None

    with open(caminho_arquivo) as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv, delimiter=';')
        lista = list(leitor)

    return lista
