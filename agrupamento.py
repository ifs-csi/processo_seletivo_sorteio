def gerar_resultado(candidatos):
    candidatos_ordenados = ordenar_numero_sorteado(candidatos)
    candidatos_agrupados = agrupar_candidatos(candidatos_ordenados)
    definir_colocacao(candidatos_agrupados)

    return candidatos_agrupados

def ordenar_numero_inscricao(candidatos):
    def key_function(candidato):
        return candidato['numero_inscricao']

    candidatos_ordenados = _ordernar(candidatos, key_function)

    return candidatos_ordenados

def ordenar_numero_sorteado(candidatos):
    def key_function(candidato):
        return candidato['numero_sorteado']

    candidatos_ordenados = _ordernar(candidatos, key_function)

    return candidatos_ordenados

def _ordernar(candidatos, key_function):
    candidatos_ordenados = candidatos.copy()
    candidatos_ordenados.sort(reverse=True, key=key_function)

    return candidatos_ordenados

def agrupar_candidatos(candidatos):
    dicionario = {}

    for candidato in candidatos:
        _criar_chaves_inexistentes(dicionario, candidato)
        campus = candidato['campus']
        curso = candidato['curso']
        cota = candidato['cota']

        dicionario[campus][curso][cota].append(candidato)

    return dicionario

def _criar_chaves_inexistentes(dicionario, candidato):
    chave_campus = candidato['campus']
    if not (chave_campus in dicionario):
        dicionario[chave_campus] = {}

    campus = dicionario[chave_campus]
    chave_curso = candidato['curso']
    if not (chave_curso in campus):
        campus[chave_curso] = {}

    curso = campus[chave_curso]
    cota = candidato['cota']
    if not (cota in curso):
        curso[cota] = []

def definir_colocacao(candidatos_agrupados):
    for _, cursos in candidatos_agrupados.items():
        for _, cotas in cursos.items():
            for _, candidatos in cotas.items():
                posicao = 0
                for candidato in candidatos:
                    posicao += 1
                    candidato['posicao'] = posicao
