import filecmp
import os
import unittest

import output_html

from .output_constantes import CANDIDATOS

ARQUIVO_TESTE = 'test_files/resultado.html'
ARQUIVO_TEMPORARIO_COMPARACAO = 'test_files/tmp.html'


class TestOutputHTML(unittest.TestCase):
    def test_escrever_resultado(self):
        output_html.escrever_arquivo_resultado(
            ARQUIVO_TEMPORARIO_COMPARACAO,
            CANDIDATOS,
        )

        self.assertTrue(
            filecmp.cmp(ARQUIVO_TESTE, ARQUIVO_TEMPORARIO_COMPARACAO)
        )
        os.remove(ARQUIVO_TEMPORARIO_COMPARACAO)
