import unittest

import input_csv

class TestInputCSV(unittest.TestCase):
    def test_carregar_lista_nao_formatada(self):
        lista = input_csv.carregar_lista('test_files/lista.csv')

        self.assertEqual(lista[0]['campus'], 'CAMPUS ARACAJU')
        self.assertEqual(
            lista[0]['curso'],
            'Curso Técnico de Nível Médio em Alimentos'
        )
        self.assertEqual(lista[0]['cota'], 'Grupo A - Ampla Concorrência')
        self.assertEqual(lista[0]['numero_inscricao'], '25086')
        self.assertEqual(lista[0]['nome'], 'FULANO DE TAL')
        self.assertEqual(lista[0]['numero_sorteado'], '419326372')
