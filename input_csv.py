import csv

def carregar_lista_formatada(caminho_arquivo):
    lista = carregar_lista(caminho_arquivo)
    lista_formatada = formatar_lista(lista)

    return lista_formatada

def carregar_lista(caminho_arquivo):
    lista = None

    with open(caminho_arquivo) as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv, delimiter=';')
        lista = list(leitor)

    return lista

def formatar_lista(lista):
    lista_formatada = []

    for linha in lista:
        linha_formatada = {
            'campus': linha['campus'],
            'curso': linha['curso'],
            'cota': linha['cota'],
            'numero_inscricao': int(linha['numero_inscricao']),
            'nome': linha['nome'],
            'numero_sorteado': int(linha['numero_sorteado']),
        }
        lista_formatada.append(linha_formatada)

    return lista_formatada
