import csv


def escrever_arquivo_resultado(nome_arquivo, resultado):
    with open(nome_arquivo, 'w') as arquivo_csv:
        campos = [
            'campus',
            'curso',
            'regime',
            'cota',
            'posicao',
            'numero_inscricao',
            'nome',
            'numero_sorteado',
        ]
        writer = csv.DictWriter(arquivo_csv, fieldnames=campos)

        writer.writeheader()
        _escrever_resultado_candidatos(writer, resultado)


def _escrever_resultado_candidatos(writer, resultado):
    candidatos = _converter_resultado_candidatos(resultado)

    for candidato in candidatos:
        _escrever_candidato(writer, candidato)


def _converter_resultado_candidatos(resultado):
    candidatos = []
    for _, cursos in resultado.items():
        for _, regimes in cursos.items():
            for _, cotas in regimes.items():
                for _, candidatos_cotas in cotas.items():
                    candidatos.extend(candidatos_cotas)
    return candidatos


def _escrever_candidato(writer, candidato):
    writer.writerow(candidato)
