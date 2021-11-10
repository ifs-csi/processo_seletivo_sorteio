#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import agrupamento
import input_csv
import output_csv
import output_html
import sorteador_adapter
import sorteio


def main():
    seed = get_seed()
    sorteador = sorteador_adapter.Sorteador(seed)

    candidatos = get_candidatos()
    sortear(sorteador, candidatos)
    quantidade_vagas = get_quantidade_vagas()
    resultado = gerar_resultado(candidatos, quantidade_vagas)

    escrever_arquivo(resultado)


def get_seed():
    return int(sys.argv[1])


def get_quantidade_vagas():
    arquivo = sys.argv[2]

    quantidade_vagas = input_csv.carregar_dict_vagas_formatada(arquivo)

    return quantidade_vagas


def get_candidatos():
    arquivo = sys.argv[3]

    candidatos = input_csv.carregar_lista_candidatos_formatada(arquivo)
    candidatos_ordenados = agrupamento.ordenar_numero_inscricao(candidatos)

    return candidatos_ordenados


def sortear(sorteador, candidatos):
    sorteio.sortear_numeros_candidatos(candidatos, sorteador)


def gerar_resultado(candidatos, quantidade_vagas):
    return agrupamento.gerar_resultado(candidatos, quantidade_vagas)


def escrever_arquivo(resultado):
    tipo_arquivo = sys.argv[4].lower()
    arquivo_resultado = sys.argv[5]

    if tipo_arquivo == 'csv':
        output_csv.escrever_arquivo_resultado(arquivo_resultado, resultado)
    elif tipo_arquivo == 'html':
        output_html.escrever_arquivo_resultado(arquivo_resultado, resultado)
    else:
        raise ValueError(
            'Não é possível gerar um arquivo do tipo "{}".'.format(
                tipo_arquivo
            )
        )


if __name__ == '__main__':
    main()
