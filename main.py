#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import sorteador_adapter
import input_csv
import agrupamento
import sorteio
import output_csv

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
    arquivo_resultado = sys.argv[3]
    output_csv.escrever_arquivo_resultado(arquivo_resultado, resultado)

if __name__ == '__main__':
    main()
