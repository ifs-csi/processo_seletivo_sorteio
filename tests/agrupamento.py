import unittest
import random

import agrupamento

CAMPI = [
    'Aracaju',
    'São Cristóvão',
    'Lagarto',
    'Itabaiana',
    'Estância',
    'Glória',
    'Tobias Barreto',
    'Propriá',
    'Socorro',
]

CURSOS = [
    'Edificações',
    'Química',
    'Informática',
    'Eletromecânica',
    'Laticínios',
    'Agronomia'
]

COTAS = ['Cota A', 'Cota B', 'Cota C']

def gerar_lista_candidatos():
    candidatos = []

    for i in range(0, 100):
        candidato = gerar_candidato_aleatorio()
        candidatos.append(candidato)

    return candidatos

def gerar_candidato_aleatorio():
    campus = get_campus_aleatorio()
    curso = get_curso_aleatorio()
    cota = get_cota_aleatoria()
    numero_inscricao = get_numero_aleatorio()
    numero_sorteado = get_numero_aleatorio()

    candidato = {
        'campus': campus,
        'curso': curso,
        'cota': cota,
        'numero_inscricao': numero_inscricao,
        'numero_sorteado': numero_sorteado,
    }

    return candidato

def get_campus_aleatorio():
    codigo_campus = random.randint(0, 8)

    return CAMPI[codigo_campus]

def get_curso_aleatorio():
    codigo_curso = random.randint(0, 5)

    return CURSOS[codigo_curso]

def get_cota_aleatoria():
    codigo_cota = random.randint(0, 2)

    return COTAS[codigo_cota]

def get_numero_aleatorio():
    return random.randint(1, 2**32)

class TestAgrupamento(unittest.TestCase):
    def test_ordenar_por_numero_inscricao(self):
        candidatos = gerar_lista_candidatos()
        candidatos_ordenados = agrupamento.ordenar_numero_inscricao(candidatos)

        ultimo_candidato = None
        for candidato in candidatos_ordenados:
            if ultimo_candidato is not None:
                self.assertLessEqual(
                    candidato['numero_inscricao'],
                    ultimo_candidato['numero_inscricao']
                )

            ultimo_candidato = candidato

    def test_ordenar_por_numero_sorteado(self):
        candidatos = gerar_lista_candidatos()
        candidatos_ordenados = agrupamento.ordenar_numero_sorteado(candidatos)

        ultimo_candidato = None
        for candidato in candidatos_ordenados:
            if ultimo_candidato is not None:
                self.assertLessEqual(
                    candidato['numero_sorteado'],
                    ultimo_candidato['numero_sorteado']
                )

            ultimo_candidato = candidato

    def test_agrupar(self):
        candidatos = gerar_lista_candidatos()
        candidatos_agrupados = agrupamento.agrupar_candidatos(candidatos)

        for campus, candidatos_campus in candidatos_agrupados.items():
            for curso, candidatos_curso in candidatos_campus.items():
                for cota, candidatos_cota in candidatos_curso.items():
                    candidatos_selecionados = []

                    for candidato in candidatos:
                        if (
                            (candidato['campus'] == campus)
                            and (candidato['curso'] == curso)
                            and (candidato['cota'] == cota)
                        ):
                            candidatos_selecionados.append(candidato)
                    self.assertEqual(candidatos_cota, candidatos_selecionados)

    def test_gerar_resultado(self):
        candidatos = gerar_lista_candidatos()
        resultado = agrupamento.gerar_resultado(candidatos)
        ultimo_campus = None

        for campus, candidatos_campus in resultado.items():
            ultimo_curso = None

            if ultimo_campus is not None:
                self.assertLessEqual(ultimo_campus, campus)

            for curso, candidatos_curso in candidatos_campus.items():
                ultima_cota = None

                if ultimo_curso is not None:
                    self.assertLessEqual(ultimo_curso, curso)

                for cota, candidatos_cota in candidatos_curso.items():
                    ultimo_candidato = None

                    if ultima_cota is not None:
                        self.assertLessEqual(ultima_cota, cota)

                    for candidato in candidatos_cota:
                        if ultimo_candidato is not None:
                            self.assertLessEqual(
                                candidato['numero_sorteado'],
                                ultimo_candidato['numero_sorteado'],
                            )
                            self.assertLessEqual(
                                ultimo_candidato['posicao'],
                                candidato['posicao'],
                            )

                        ultimo_candidato = candidato

                    ultima_cota = cota

                ultimo_curso = curso

            ultimo_campus = campus

    def test_definir_colocacao(self):
        candidatos = gerar_lista_candidatos()
        candidatos_ordenados = agrupamento.ordenar_numero_sorteado(candidatos)
        candidatos_agrupados = agrupamento.agrupar_candidatos(
            candidatos_ordenados
        )
        agrupamento.definir_colocacao(candidatos_agrupados)

        for campus, candidatos_campus in candidatos_agrupados.items():
            for curso, candidatos_curso in candidatos_campus.items():
                for cota, candidatos_cota in candidatos_curso.items():
                    ultimo_candidato = None
                    for candidato in candidatos_cota:
                        if ultimo_candidato is not None:
                            self.assertLessEqual(
                                ultimo_candidato['posicao'],
                                candidato['posicao'],
                            )

                        ultimo_candidato = candidato
