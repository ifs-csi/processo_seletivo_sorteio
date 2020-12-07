def ordenar_numero_sorteado(candidatos):
    def key_function(candidato):
        return candidato['numero_sorteado']

    candidatos_ordenados = candidatos.copy()
    candidatos_ordenados.sort(reverse=True, key=key_function)

    return candidatos_ordenados
