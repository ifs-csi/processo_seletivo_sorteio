import unittest

import agrupamento

class TestAgrupamento(unittest.TestCase):
    def test_ordenar(self):
        candidato1 = {
            'campus': 'Aracaju',
            'curso': 'Edificações',
            'cota': 'cota a',
            'numero_sorteado': 30
        }
        candidato2 = {
            'campus': 'Lagarto',
            'curso': 'Edificações',
            'cota': 'cota a',
            'numero_sorteado': 101
        }
        candidato3 = {
            'campus': 'Aracaju',
            'curso': 'Química',
            'cota': 'cota b',
            'numero_sorteado': 47
        }
        candidato4 = {
            'campus': 'Aracaju',
            'curso': 'Edificações',
            'cota': 'cota a',
            'numero_sorteado': 22
        }
        candidato5 = {
            'campus': 'Aracaju',
            'curso': 'Química',
            'cota': 'cota b',
            'numero_sorteado': 19
        }
        candidato6 = {
            'campus': 'Lagarto',
            'curso': 'Edificações',
            'cota': 'cota a',
            'numero_sorteado': 3
        }

        candidatos = [
            candidato1,
            candidato2,
            candidato3,
            candidato4,
            candidato5,
            candidato6
        ]

        candidatos_ordenados = agrupamento.ordenar_numero_sorteado(candidatos)

        self.assertEqual(candidatos_ordenados[0], candidato2)
        self.assertEqual(candidatos_ordenados[1], candidato3)
        self.assertEqual(candidatos_ordenados[2], candidato1)
        self.assertEqual(candidatos_ordenados[3], candidato4)
        self.assertEqual(candidatos_ordenados[4], candidato5)
        self.assertEqual(candidatos_ordenados[5], candidato6)
