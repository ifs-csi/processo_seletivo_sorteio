import random
import unittest

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

REGIMES = ['Semi-Interno', 'Interno (Masculino)', 'Interno (Feminino)']

COTAS = ['Cota A', 'Cota B', 'Cota C']


def gerar_quantidade_vagas(candidatos):
    quantidade_cagas = {}

    for candidato in candidatos:
        nome_campus = candidato['campus']
        nome_curso = candidato['curso']
        descricao_regime = candidato['regime']
        nome_cota = candidato['cota']

        if nome_campus not in quantidade_cagas:
            campus = {}
            quantidade_cagas[nome_campus] = campus
        campus = quantidade_cagas[nome_campus]
        if nome_curso not in campus:
            curso = {}
            campus[nome_curso] = curso
        curso = campus[nome_curso]
        if descricao_regime not in curso:
            regime = {}
            curso[descricao_regime] = regime
        regime = curso[descricao_regime]
        regime[nome_cota] = random.randint(0, 3)

    return quantidade_cagas


def gerar_lista_candidatos():
    candidatos = []

    for i in range(0, 100):
        candidato = gerar_candidato_aleatorio()
        candidatos.append(candidato)

    return candidatos


def gerar_candidato_aleatorio():
    campus = random.choice(CAMPI)
    curso = random.choice(CURSOS)
    regime = random.choice(REGIMES)
    cota = random.choice(COTAS)
    numero_inscricao = get_numero_aleatorio()
    numero_sorteado = get_numero_aleatorio()

    candidato = {
        'campus': campus,
        'curso': curso,
        'regime': regime,
        'cota': cota,
        'numero_inscricao': numero_inscricao,
        'numero_sorteado': numero_sorteado,
    }

    return candidato


def get_numero_aleatorio():
    return random.randint(1, 2**32)


class TestAgrupamento(unittest.TestCase):
    def test_ordenar_por_numero_inscricao(self):
        candidatos = gerar_lista_candidatos()
        candidatos_ordenados = agrupamento.ordenar_numero_inscricao(candidatos)

        ultimo_candidato = None
        for candidato in candidatos_ordenados:
            if ultimo_candidato is not None:
                self.assertLessEqual(
                    candidato['numero_inscricao'],
                    ultimo_candidato['numero_inscricao']
                )

            ultimo_candidato = candidato

    def test_ordenar_por_numero_sorteado(self):
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
                for regime, candidatos_regime in candidatos_curso.items():
                    for cota, candidatos_cota in candidatos_regime.items():
                        candidatos_selecionados = []

                        for candidato in candidatos:
                            if (
                                (candidato['campus'] == campus)
                                and (candidato['curso'] == curso)
                                and (candidato['regime'] == regime)
                                and (candidato['cota'] == cota)
                            ):
                                candidatos_selecionados.append(candidato)
                        self.assertEqual(
                            candidatos_cota,
                            candidatos_selecionados
                        )

    def test_gerar_resultado(self):
        candidatos = gerar_lista_candidatos()
        quantidade_vagas = gerar_quantidade_vagas(candidatos)
        resultado = agrupamento.gerar_resultado(candidatos, quantidade_vagas)
        ultimo_campus = None

        for campus, candidatos_campus in resultado.items():
            vagas_campus = quantidade_vagas[campus]
            ultimo_curso = None

            if ultimo_campus is not None:
                self.assertLessEqual(ultimo_campus, campus)

            for curso, candidatos_curso in candidatos_campus.items():
                vagas_curso = vagas_campus[curso]
                ultima_regime = None

                if ultimo_curso is not None:
                    self.assertLessEqual(ultimo_curso, curso)

                for regime, candidatos_regime in candidatos_curso.items():
                    vagas_regime = vagas_curso[regime]
                    ultima_cota = None

                    if ultima_regime is not None:
                        self.assertLessEqual(ultimo_regime, regime)

                    for cota, candidatos_cota in candidatos_regime.items():
                        vagas_cota = vagas_regime[cota]
                        ultimo_candidato = None

                        if ultima_cota is not None:
                            self.assertLessEqual(ultima_cota, cota)

                        for candidato in candidatos_cota:
                            if ultimo_candidato is not None:
                                self.assertLessEqual(
                                    candidato['numero_sorteado'],
                                    ultimo_candidato['numero_sorteado'],
                                )
                                self.assertLessEqual(
                                    ultimo_candidato['posicao'],
                                    candidato['posicao'],
                                )

                            situacao_esperada = agrupamento.APROVADO
                            if candidato['posicao'] > vagas_cota:
                                situacao_esperada = agrupamento.EXCEDENTE
                            self.assertEquals(
                                situacao_esperada,
                                candidato['situacao'],
                            )
                            ultimo_candidato = candidato

                        ultima_cota = cota

                    ultimo_regime = regime

                ultimo_curso = curso

            ultimo_campus = campus

    def test_definir_colocacao(self):
        candidatos = gerar_lista_candidatos()
        candidatos_ordenados = agrupamento.ordenar_numero_sorteado(candidatos)
        candidatos_agrupados = agrupamento.agrupar_candidatos(
            candidatos_ordenados
        )
        agrupamento.definir_colocacao(candidatos_agrupados)

        for _, candidatos_campus in candidatos_agrupados.items():
            for _, candidatos_curso in candidatos_campus.items():
                for _, candidatos_regime in candidatos_curso.items():
                    for _, candidatos_cota in candidatos_regime.items():
                        ultimo_candidato = None
                        for candidato in candidatos_cota:
                            if ultimo_candidato is not None:
                                self.assertLessEqual(
                                    ultimo_candidato['posicao'],
                                    candidato['posicao'],
                                )

                            ultimo_candidato = candidato
