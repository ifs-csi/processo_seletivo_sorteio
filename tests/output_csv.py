import unittest
import filecmp
import os

import output_csv

CANDIDATOS = {
    'CAMPUS ARACAJU': {
        'Curso Técnico de Nível Médio em Alimentos': {
            'Grupo A - Ampla Concorrência': [
                {
                   'campus': 'CAMPUS ARACAJU',
                   'curso': 'Curso Técnico de Nível Médio em Alimentos',
                   'cota': 'Grupo A - Ampla Concorrência',
                   'posicao': '1',
                   'numero_inscricao': '25086',
                   'nome': 'FULANO DE TAL',
                   'numero_sorteado': '3751169278',
                },
            ],
        },
        'Curso Técnico de Nível Médio em Química': {
            'Grupo B - Outros': [
                {
                    'campus': 'CAMPUS ARACAJU',
                    'curso': 'Curso Técnico de Nível Médio em Química',
                    'cota': 'Grupo B - Outros',
                    'posicao': '1',
                    'numero_inscricao': '25097',
                    'nome': 'CICRANO DE TAL',
                    'numero_sorteado': '3178489223',
                },
                {
                    'campus': 'CAMPUS ARACAJU',
                    'curso': 'Curso Técnico de Nível Médio em Química',
                    'cota': 'Grupo B - Outros',
                    'posicao': '2',
                    'numero_inscricao': '25186',
                    'nome': 'CONSECTETUR ADIPISCING ELIT',
                    'numero_sorteado': '1916507804',
                },
            ],
            'Grupo A - Ampla Concorrência': [
                {
                    'campus': 'CAMPUS ARACAJU',
                    'curso': 'Curso Técnico de Nível Médio em Química',
                    'cota': 'Grupo A - Ampla Concorrência',
                    'posicao': '1',
                    'numero_inscricao': '35086',
                    'nome': 'LOREM IPSUM',
                    'numero_sorteado': '662124364',
                },
            ],
        },
    },
    'CAMPUS LAGARTO': {
        'Curso Técnico de Nível Médio em Alimentos': {
            'Grupo C - PPI': [
                {
                    'campus': 'CAMPUS LAGARTO',
                    'curso': 'Curso Técnico de Nível Médio em Alimentos',
                    'cota': 'Grupo C - PPI',
                    'posicao': '1',
                    'numero_inscricao': '9506',
                    'nome': 'BELTRANO DE TAL',
                    'numero_sorteado': '2292393220',
                },
            ],
        },
    },
    'CAMPUS SOCORRO': {
        'Curso Técnico de Nível Médio em Alimentos': {
            'Grupo A - Ampla Concorrência': [
                {
                    'campus': 'CAMPUS SOCORRO',
                    'curso': 'Curso Técnico de Nível Médio em Alimentos',
                    'cota': 'Grupo A - Ampla Concorrência',
                    'posicao': '1',
                    'numero_inscricao': '25085',
                    'nome': 'SED DO EIUSMOD',
                    'numero_sorteado': '1130929394',
                },
            ],
        },
    },
    'CAMPUS ESTANCIA': {
        'Curso Técnico de Nível Médio em Alimentos': {
            'Grupo A - Ampla Concorrência': [
                {
                    'campus': 'CAMPUS ESTANCIA',
                    'curso': 'Curso Técnico de Nível Médio em Alimentos',
                    'cota': 'Grupo A - Ampla Concorrência',
                    'posicao': '1',
                    'numero_inscricao': '24086',
                    'nome': 'DOLOR SIT AMET',
                    'numero_sorteado': '371232387',
                },
            ],
        },
    },
}

ARQUIVO_TESTE = 'test_files/resultado.csv'
ARQUIVO_TEMPORARIO_COMPARACAO = 'test_files/tmp.csv'

class TestOutputCSV(unittest.TestCase):
    def test_escrever_resultado(self):
        output_csv.escrever_arquivo_resultado(
            ARQUIVO_TEMPORARIO_COMPARACAO,
            CANDIDATOS,
        )

        self.assertTrue(
            filecmp.cmp(ARQUIVO_TESTE, ARQUIVO_TEMPORARIO_COMPARACAO)
        )
        os.remove(ARQUIVO_TEMPORARIO_COMPARACAO)
