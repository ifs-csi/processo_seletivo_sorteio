import csv


def carregar_lista_candidatos_formatada(caminho_arquivo):
    def formatar(lista):
        lista_formatada = []

        for linha in lista:
            linha_formatada = {
                'campus': linha['campus'],
                'curso': linha['curso'],
                'regime': linha['regime'],
                'cota': linha['cota'],
                'numero_inscricao': int(linha['numero_inscricao']),
                'nome': linha['nome'],
            }
            lista_formatada.append(linha_formatada)

        return lista_formatada

    return _carregar_arquivo_formatado(caminho_arquivo, formatar)


def carregar_dict_vagas_formatada(caminho_arquivo):
    def formatar(lista):
        dict_formatada = {}

        for linha in lista:
            nome_campus = linha['campus']
            nome_curso = linha['curso']
            descricao_regime = linha['regime']
            nome_cota = linha['cota']
            numero_vagas = int(linha['numero_vagas'])

            if nome_campus not in dict_formatada:
                campus = {}
                dict_formatada[nome_campus] = campus
            campus = dict_formatada[nome_campus]
            if nome_curso not in campus:
                curso = {}
                campus[nome_curso] = curso
            curso = campus[nome_curso]
            if descricao_regime not in curso:
                regime = {}
                curso[descricao_regime] = regime
            regime = curso[descricao_regime]
            regime[nome_cota] = numero_vagas

        return dict_formatada

    return _carregar_arquivo_formatado(caminho_arquivo, formatar)


def _carregar_arquivo_formatado(caminho_arquivo, formatador):
    lista = _carregar_lista(caminho_arquivo)
    lista_formatada = formatador(lista)

    return lista_formatada


def _carregar_lista(caminho_arquivo):
    lista = None

    with open(caminho_arquivo) as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv, delimiter=';')
        lista = list(leitor)

    return lista
