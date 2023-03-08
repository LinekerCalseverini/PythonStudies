#!/usr/local/bin/python3
# Exercício (clássico): cálculo de IMC
# Como já conseguimos trabalhar com argumentos, estou testando variáveis de ambiente no docker
import os
nome = os.environ['NOME']
altura = os.environ['ALTURA']
peso = os.environ['PESO']
imc = peso / altura ** 2

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

print(f'{nome} tem {altura} de altura, pesa {peso} e seu IMC é {imc}')