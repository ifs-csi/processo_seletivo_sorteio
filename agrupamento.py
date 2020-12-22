from collections import OrderedDict

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
    candidatos_agrupados = {}

    for candidato in candidatos:
        _criar_chaves_inexistentes(candidatos_agrupados, candidato)
        campus = candidato['campus']
        curso = candidato['curso']
        cota = candidato['cota']

        candidatos_agrupados[campus][curso][cota].append(candidato)

    return _ordenar_grupos_candidatos(candidatos_agrupados)

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

def _ordenar_grupos_candidatos(candidatos_agrupados):
    candidatos_agrupados_ordenados = OrderedDict()

    for campus, candidatos_cursos in sorted(
        candidatos_agrupados.items(),
        key=lambda x: x[0]
    ):
        candidatos_campus_ordenados = OrderedDict()
        candidatos_agrupados_ordenados[campus] = candidatos_campus_ordenados
        for curso, candidatos_cotas in sorted(
            candidatos_cursos.items(),
            key=lambda x: x[0]
        ):
            candidatos_cursos_ordenados = OrderedDict()
            candidatos_campus_ordenados[curso] = candidatos_cursos_ordenados
            for cota, candidatos in sorted(
                candidatos_cotas.items(),
                key=lambda x: x[0]
            ):
                candidatos_cursos_ordenados[cota] = candidatos

    return candidatos_agrupados_ordenados

def definir_colocacao(candidatos_agrupados):
    for _, cursos in candidatos_agrupados.items():
        for _, cotas in cursos.items():
            for _, candidatos in cotas.items():
                posicao = 0
                for candidato in candidatos:
                    posicao += 1
                    candidato['posicao'] = posicao
