#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import sorteador_adapter
import input_csv
import agrupamento
import sorteio
import output_csv
import output_html

def main():
    seed = get_seed()
    sorteador = sorteador_adapter.Sorteador(seed)

    candidatos = get_candidatos()
    sortear(sorteador, candidatos)
    resultado = gerar_resultado(candidatos)

    escrever_arquivo(resultado)

def get_seed():
    return int(sys.argv[1])

def get_candidatos():
    arquivo = sys.argv[2]

    candidatos = input_csv.carregar_lista_formatada(arquivo)
    candidatos_ordenados = agrupamento.ordenar_numero_inscricao(candidatos)

    return candidatos_ordenados

def sortear(sorteador, candidatos):
    sorteio.sortear_numeros_candidatos(candidatos, sorteador)

def gerar_resultado(candidatos):
    return agrupamento.gerar_resultado(candidatos)

def escrever_arquivo(resultado):
    tipo_arquivo = sys.argv[3].lower()
    arquivo_resultado = sys.argv[4]

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
