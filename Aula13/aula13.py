#!/usr/local/bin/python3
# F-Strings
# São uma maneira de formatar strings, ela se dá pela seguinte sintaxe:
# str = f'<string>{variavel}'
# Dessa maneira, o interpretador vai inserir as variáveis no meio da string

# Comando docker para rodar esse container:
# docker run --rm -e "NOME={nome}" -e "PESO={peso}" -e "ALTURA={altura}" python:aula13

import os
nome = os.environ['NOME']
altura = float(os.environ['ALTURA'])
peso = float(os.environ['PESO'])
imc = peso / altura ** 2

# Como podemos ver abaixo, podemos formatar a quantidade de casas em um número float usando a expressão 'variavel:.<numero>f'
# Caso queiramos trocar o ponto pela vírgula, podemos usar 'variavel:,.<numero>f'

linha1 = f'{nome} tem {altura:,.2f} de altura,'
linha2 = f'pesa {peso} e seu IMC é'
linha3 = f'{imc:,.2f}'

print(linha1)
print(linha2)
print(linha3)