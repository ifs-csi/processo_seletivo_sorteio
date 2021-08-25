import unittest

import input_csv


class TestInputCSV(unittest.TestCase):
    def test_carregar_lista_nao_formatada(self):
        lista = input_csv.carregar_lista('test_files/lista.csv')
        candidato = lista[0]

        self.assertEqual(candidato['campus'], 'CAMPUS ARACAJU')
        self.assertEqual(
            candidato['curso'],
            'Curso Técnico de Nível Médio em Alimentos'
        )
        self.assertEqual(candidato['regime'], 'Semi-Interno')
        self.assertEqual(candidato['cota'], 'Grupo A - Ampla Concorrência')
        self.assertEqual(candidato['numero_inscricao'], '25086')
        self.assertEqual(candidato['nome'], 'FULANO DE TAL')

    def test_formatar_lista(self):
        lista = []
        linha = {
            'campus': 'CAMPUS ARACAJU',
            'curso': 'Curso Técnico de Nível Médio em Alimentos',
            'regime': 'Interno',
            'cota': 'Grupo A - Ampla Concorrência',
            'numero_inscricao': '25086',
            'nome': 'FULANO DE TAL',
        }
        lista.append(linha)

        lista_formatada = input_csv.formatar_lista(lista)
        candidato = lista_formatada[0]

        self.assertEqual(candidato['campus'], 'CAMPUS ARACAJU')
        self.assertEqual(
            candidato['curso'],
            'Curso Técnico de Nível Médio em Alimentos'
        )
        self.assertEqual(
            candidato['cota'],
            'Grupo A - Ampla Concorrência'
        )
        self.assertEqual(candidato['numero_inscricao'], 25086)
        self.assertEqual(candidato['nome'], 'FULANO DE TAL')

    def test_carregar_lista_formatada(self):
        lista = input_csv.carregar_lista_formatada('test_files/lista.csv')
        candidato = lista[0]

        self.assertEqual(candidato['campus'], 'CAMPUS ARACAJU')
        self.assertEqual(
            candidato['curso'],
            'Curso Técnico de Nível Médio em Alimentos'
        )
        self.assertEqual(candidato['regime'], 'Semi-Interno')
        self.assertEqual(candidato['cota'], 'Grupo A - Ampla Concorrência')
        self.assertEqual(candidato['numero_inscricao'], 25086)
        self.assertEqual(candidato['nome'], 'FULANO DE TAL')
