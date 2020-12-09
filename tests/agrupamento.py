import unittest

import agrupamento

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
    'numero_sorteado': 101
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
    'numero_sorteado': 3
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
        candidatos_ordenados = agrupamento.ordenar_numero_sorteado(CANDIDATOS)

        self.assertEqual(candidatos_ordenados[0], CANDIDATO2)
        self.assertEqual(candidatos_ordenados[1], CANDIDATO3)
        self.assertEqual(candidatos_ordenados[2], CANDIDATO1)
        self.assertEqual(candidatos_ordenados[3], CANDIDATO4)
        self.assertEqual(candidatos_ordenados[4], CANDIDATO5)
        self.assertEqual(candidatos_ordenados[5], CANDIDATO6)

    def test_agrupar(self):
        candidatos_agrupados = agrupamento.agrupar_candidatos(CANDIDATOS)

        self.assertEqual(
            [CANDIDATO1, CANDIDATO4],
            candidatos_agrupados['Aracaju']['Edificações']['cota a']
        )
        self.assertEqual(
            [CANDIDATO2, CANDIDATO6],
            candidatos_agrupados['Lagarto']['Edificações']['cota a']
        )
        self.assertEqual(
            [CANDIDATO3, CANDIDATO5],
            candidatos_agrupados['Aracaju']['Química']['cota b']
        )
