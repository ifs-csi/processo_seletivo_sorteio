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
    numero_sorteado = get_numero_sorteado_aleatorio()

    candidato = {
        'campus': campus,
        'curso': curso,
        'cota': cota,
        'numero_sorteado': numero_sorteado
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

def get_numero_sorteado_aleatorio():
    return random.randint(1, 2**32)

CANDIDATO1 = {
    'campus': 'Aracaju',
    'curso': 'Edificações',
    'cota': 'cota a',
    'numero_sorteado': 30
}
CANDIDATO2 = {
    'campus': 'Lagarto',
    'curso': 'Edificações',
    'cota': 'cota a',
    'numero_sorteado': 3
}
CANDIDATO3 = {
    'campus': 'Aracaju',
    'curso': 'Química',
    'cota': 'cota b',
    'numero_sorteado': 47
}
CANDIDATO4 = {
    'campus': 'Aracaju',
    'curso': 'Edificações',
    'cota': 'cota a',
    'numero_sorteado': 22
}
CANDIDATO5 = {
    'campus': 'Aracaju',
    'curso': 'Química',
    'cota': 'cota b',
    'numero_sorteado': 19
}
CANDIDATO6 = {
    'campus': 'Lagarto',
    'curso': 'Edificações',
    'cota': 'cota a',
    'numero_sorteado': 101
}

CANDIDATOS = [
    CANDIDATO1,
    CANDIDATO2,
    CANDIDATO3,
    CANDIDATO4,
    CANDIDATO5,
    CANDIDATO6
]

class TestAgrupamento(unittest.TestCase):
    def test_ordenar(self):
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
        resultado = agrupamento.gerar_resultado(CANDIDATOS)

        self.assertEqual(
            [CANDIDATO1, CANDIDATO4],
            resultado['Aracaju']['Edificações']['cota a']
        )
        self.assertEqual(
            [CANDIDATO6, CANDIDATO2],
            resultado['Lagarto']['Edificações']['cota a']
        )
        self.assertEqual(
            [CANDIDATO3, CANDIDATO5],
            resultado['Aracaju']['Química']['cota b']
        )
