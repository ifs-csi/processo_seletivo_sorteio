import unittest

import sorteio

class SorteadorMock:
    def __init__(self):
        self.index = 0

    def sortear(self):
        self.index += 1
        return self.index - 1

class SorteadorNumerosRepetidosMock:
    def __init__(self):
        self.index = 0

    def sortear(self):
        self.index += 1
        return self.index // 2

class TestSorteio(unittest.TestCase):
    def test_atribuir_numero_sorteado(self):
        sorteador = SorteadorMock()
        for i in range(0, 100):
            candidato = {}
            sorteio.sortear_numero_candidato(candidato, sorteador)
            self.assertEqual(i, candidato['numero_sorteado'])

    def test_atribuir_numeros_sorteados_lista(self):
        sorteador = SorteadorMock()

        candidatos = []
        for i in range(0, 100):
            candidato = {}
            candidatos.append(candidato)

        sorteio.sortear_numeros_candidatos(candidatos, sorteador)

        for i in range(0, 100):
            candidato = candidatos[i]
            self.assertEqual(i, candidato['numero_sorteado'])

    def test_numero_ja_sorteado(self):
        candidatos = []
        for i in range(0, 100):
            candidato = {'numero_sorteado': i}
            candidatos.append(candidato)

        for i in range(0, 100):
            candidato = {'numero_sorteado': i}
            self.assertTrue(sorteio.numero_ja_sorteado(candidato, candidatos))

        for i in range(100, 200):
            candidato = {'numero_sorteado': i}
            self.assertFalse(sorteio.numero_ja_sorteado(candidato, candidatos))

    def test_atribuir_numeros_unicos_sorteados_lista(self):
        sorteador = SorteadorNumerosRepetidosMock()

        candidatos = []
        for i in range(0, 100):
            candidato = {}
            candidatos.append(candidato)

        sorteio.sortear_numeros_candidatos(candidatos, sorteador)

        for i in range(0, 100):
            candidato = candidatos[i]
            self.assertEqual(i, candidato['numero_sorteado'])
