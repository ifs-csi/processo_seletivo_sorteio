#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import sorteador_adapter
import input_csv
import agrupamento
import sorteio

def main():
    preparar()

    candidatos = get_candidatos()
    sortear(candidatos)
    resultado = gerar_resultado(candidatos)

    print(resultado)

def preparar():
    seed = int(sys.argv[1])
    sorteador_adapter.definir_seed(seed)

def get_candidatos():
    arquivo = sys.argv[2]

    candidatos = input_csv.carregar_lista_formatada(arquivo)
    candidatos_ordenados = agrupamento.ordenar_numero_inscricao(candidatos)

    return candidatos_ordenados

def sortear(candidatos):
    sorteio.sortear_numeros_candidatos(candidatos, sorteador_adapter.sorteador)

def gerar_resultado(candidatos):
    return agrupamento.gerar_resultado(candidatos)

if __name__ == '__main__':
    main()
