#!/usr/local/bin/python3
# Exercício: Utilizando comparadores, escrever um programa que recebe dois valores e diz qual é o maior.
# Neste exercício tentei reutilizar o máximo possível strings, simplesmente pra ver quanto de memória eu consigo economizar. Este método tornou o código imprático e difícil de ler, porém como é um código pequeno foi um bom método para praticar.

DIGITE = 'Digite'
VALOR = 'valor'
PRIMEIRO = 'primeiro'
SEGUNDO = 'segundo'

primeiro_valor = input(f'{DIGITE} um {VALOR}: ')
segundo_valor = input(f'{DIGITE} outro {VALOR}: ')

resposta = [PRIMEIRO,primeiro_valor,SEGUNDO,segundo_valor]

if segundo_valor > primeiro_valor:
    resposta = [SEGUNDO,segundo_valor,PRIMEIRO,primeiro_valor]

if primeiro_valor != segundo_valor:
    resposta.append('maior que ')
else:
    resposta.append('igual a')

print(f'O {resposta[0]} {VALOR} ({resposta[1]}) é {resposta[4]}o {resposta[2]} {VALOR} ({resposta[3]}).')
