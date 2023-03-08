#!/usr/local/bin/python3
# Exercício (clássico): cálculo de IMC
# Como já conseguimos trabalhar com argumentos, estou testando variáveis de ambiente no docker

# Variáveis de ambiente são consideradas string para o Python, então é necessário fazer um casting.

# Comando docker para rodar esse container:
# docker run --rm -e "NOME={nome}" -e "PESO={peso}" -e "ALTURA={altura}" python:aula12
import os
nome = os.environ['NOME']
altura = float(os.environ['ALTURA'])
peso = float(os.environ['PESO'])
imc = peso / altura ** 2

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

print(f'{nome} tem {altura} de altura, pesa {peso} e seu IMC é {imc}')