from collections import OrderedDict

APROVADO = 'Aprovado'
EXCEDENTE = 'Excedente'


def gerar_resultado(candidatos, quantidade_vagas):
    candidatos_ordenados = ordenar_numero_sorteado(candidatos)
    candidatos_agrupados = agrupar_candidatos(candidatos_ordenados)
    definir_colocacao(candidatos_agrupados)
    definir_situacao(candidatos_agrupados, quantidade_vagas)

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
        regime = candidato['regime']
        cota = candidato['cota']

        candidatos_agrupados[campus][curso][regime][cota].append(candidato)

    return _ordenar_grupos_candidatos(candidatos_agrupados)


def _criar_chaves_inexistentes(dicionario, candidato):
    chave_campus = candidato['campus']
    if chave_campus not in dicionario:
        dicionario[chave_campus] = {}

    campus = dicionario[chave_campus]
    chave_curso = candidato['curso']
    if chave_curso not in campus:
        campus[chave_curso] = {}

    curso = campus[chave_curso]
    chave_regime = candidato['regime']
    if chave_regime not in curso:
        curso[chave_regime] = {}

    regime = curso[chave_regime]
    chave_cota = candidato['cota']
    if chave_cota not in regime:
        regime[chave_cota] = []


def _ordenar_grupos_candidatos(candidatos_agrupados):
    candidatos_agrupados_ordenados = OrderedDict()

    _ordenar_grupos(candidatos_agrupados, candidatos_agrupados_ordenados)

    return candidatos_agrupados_ordenados


def _ordenar_grupos(candidatos_agrupados, candidatos_agrupados_ordenados):
    for subgrupo, candidatos_subgrupo in sorted(
        candidatos_agrupados.items(),
        key=lambda x: x[0]
    ):
        if isinstance(candidatos_subgrupo, dict):
            candidatos_subgrupo_ordenados = OrderedDict()
            candidatos_agrupados_ordenados[subgrupo] = (
                candidatos_subgrupo_ordenados
            )

            _ordenar_grupos(
                candidatos_subgrupo,
                candidatos_subgrupo_ordenados,
            )
        else:
            candidatos_agrupados_ordenados[subgrupo] = candidatos_subgrupo


def definir_colocacao(candidatos_agrupados):
    for _, cursos in candidatos_agrupados.items():
        for _, regimes in cursos.items():
            for _, cotas in regimes.items():
                for _, candidatos in cotas.items():
                    posicao = 0
                    for candidato in candidatos:
                        posicao += 1
                        candidato['posicao'] = posicao


def definir_situacao(candidatos_agrupados, quantidade_vagas):
    for nome_campus, cursos in candidatos_agrupados.items():
        vagas_campus = quantidade_vagas[nome_campus]
        for nome_curso, regimes in cursos.items():
            vagas_curso = vagas_campus[nome_curso]
            for descricao_regime, cotas in regimes.items():
                vagas_regime = vagas_curso[descricao_regime]
                for nome_cota, candidatos in cotas.items():
                    vagas_cota = vagas_regime[nome_cota]
                    for candidato in candidatos:
                        if candidato['posicao'] <= vagas_cota:
                            candidato['situacao'] = APROVADO
                        else:
                            candidato['situacao'] = EXCEDENTE
