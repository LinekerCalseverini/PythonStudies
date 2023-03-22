import random

qtd_cpfs = input('Digite quantos CPFs deseja gerar: ')

try:
    for _ in range(int(qtd_cpfs)):
        cpf = ''
        for i in range(9):
            cpf += str(random.randint(0,9))

        soma = 0
        indice = 10

        for algarismo in cpf:
            soma += int(algarismo) * indice
            indice -= 1
            
        primeiro_digito = soma * 10 % 11
        primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

        cpf += str(primeiro_digito)
        soma = 0
        indice = 11

        for algarismo in cpf:
            soma += int(algarismo) * indice
            indice -= 1

        segundo_digito = soma * 10 % 11
        segundo_digito = segundo_digito if segundo_digito <= 9 else 0
        cpf += str(segundo_digito)

        cpf_gerado = ''

        for i, algarismo in enumerate(cpf):
            cpf_gerado += algarismo
            if i == 2 or i == 5:
                cpf_gerado += '.'
            if i == 8:
                cpf_gerado += '-'

        print(cpf_gerado)
except:
    print('Digite um número inteiro.')