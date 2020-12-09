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

    def test_formatar_lista(self):
        lista = []
        linha = {
            'campus': 'CAMPUS ARACAJU',
            'curso': 'Curso Técnico de Nível Médio em Alimentos',
            'cota': 'Grupo A - Ampla Concorrência',
            'numero_inscricao': '25086',
            'nome': 'FULANO DE TAL',
            'numero_sorteado': '419326372',
        }
        lista.append(linha)

        lista_formatada = input_csv.formatar_lista(lista)

        self.assertEqual(lista_formatada[0]['campus'], 'CAMPUS ARACAJU')
        self.assertEqual(
            lista[0]['curso'],
            'Curso Técnico de Nível Médio em Alimentos'
        )
        self.assertEqual(
            lista_formatada[0]['cota'],
            'Grupo A - Ampla Concorrência'
        )
        self.assertEqual(lista_formatada[0]['numero_inscricao'], 25086)
        self.assertEqual(lista_formatada[0]['nome'], 'FULANO DE TAL')
        self.assertEqual(lista_formatada[0]['numero_sorteado'], 419326372)

    def test_carregar_lista_formatada(self):
        lista = input_csv.carregar_lista_formatada('test_files/lista.csv')

        self.assertEqual(lista[0]['campus'], 'CAMPUS ARACAJU')
        self.assertEqual(
            lista[0]['curso'],
            'Curso Técnico de Nível Médio em Alimentos'
        )
        self.assertEqual(lista[0]['cota'], 'Grupo A - Ampla Concorrência')
        self.assertEqual(lista[0]['numero_inscricao'], 25086)
        self.assertEqual(lista[0]['nome'], 'FULANO DE TAL')
        self.assertEqual(lista[0]['numero_sorteado'], 419326372)
