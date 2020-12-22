def sortear_numeros_candidatos(candidatos, sorteador):
    for candidato in candidatos:
        sortear_numero_candidato(candidato, sorteador)

        while numero_ja_sorteado(candidato, candidatos):
            sortear_numero_candidato(candidato, sorteador)

def sortear_numero_candidato(candidato, sorteador):
    candidato['numero_sorteado'] = sorteador.sortear()

def numero_ja_sorteado(candidato, candidatos):
    for outro_candidato in candidatos:
        if candidato is outro_candidato:
            return False
        if not ('numero_sorteado' in outro_candidato):
            return False
        if outro_candidato['numero_sorteado'] == candidato['numero_sorteado']:
            return True

    return False
