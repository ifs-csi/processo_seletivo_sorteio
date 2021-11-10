import unittest

import input_csv


class TestInputCSV(unittest.TestCase):
    def test_carregar_lista_candidatos_formatada(self):
        candidatos = input_csv.carregar_lista_candidatos_formatada(
            'test_files/lista.csv'
        )
        candidato = candidatos[0]

        self.assertEqual(candidato['campus'], 'CAMPUS ARACAJU')
        self.assertEqual(
            candidato['curso'],
            'Curso Técnico de Nível Médio em Alimentos'
        )
        self.assertEqual(candidato['regime'], 'Semi-Interno')
        self.assertEqual(candidato['cota'], 'Grupo A - Ampla Concorrência')
        self.assertEqual(candidato['numero_inscricao'], 25086)
        self.assertEqual(candidato['nome'], 'FULANO DE TAL')

    def test_carregar_dict_vagas_formatada(self):
        vagas = input_csv.carregar_dict_vagas_formatada(
            'test_files/vagas.csv'
        )
        campus = vagas['CAMPUS ARACAJU']
        curso = campus['Curso Técnico de Nível Médio em Alimentos']
        regime = curso['Semi-Interno']
        numero_vagas = regime['Grupo A - Ampla Concorrência']

        self.assertEqual(numero_vagas, 17)
