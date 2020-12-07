def sortear_numero_candidato(candidato, sorteador):
    candidato['numero_sorteado'] = sorteador()

def sortear_numeros_candidatos(candidatos, sorteador):
    for candidato in candidatos:
        sortear_numero_candidato(candidato, sorteador)
