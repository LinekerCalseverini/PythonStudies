#!/usr/local/bin/python3
# Exercício: Utilizando comparadores, escrever um programa que recebe dois valores e diz qual é o maior.
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

resposta = ['primeiro',primeiro_valor,'segundo',segundo_valor]

if segundo_valor > primeiro_valor:
    resposta = ['segundo',segundo_valor,'primeiro',primeiro_valor]

if primeiro_valor != segundo_valor:
    resposta.append('maior que ')
else:
    resposta.append('igual a')

print(f'O {resposta[0]} valor ({resposta[1]}) é {resposta[4]}o {resposta[2]} valor ({resposta[3]}).')
