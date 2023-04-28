# Calculo do segundo dígito do CPF
# CPF: 746.824.890-70
# Colete a soma dos 9 primeiros dígitos do CPF,
# MAIS O PRIMEIRO DIGITO,
# multiplicando cada um dos valores por uma
# contagem regressiva começando de 10

#Ex.: 746.824.890-70 (746824890)
#  11 10  9  8  7  6  5  4  3  2
#  7   4  6  8  2  4  8  9  0  7
#  70  36 48 56 12 20 32 27 0  14

# Somar todos os resultados:
# 70+36+48+56+12+20+32+27+0+14 = 363
# Multiplicar o resultado anterior por 10
# 363 * 10 = 3630
# Obter o resto da divisão da conta anterior por 11
# 3630 % 11 = 0
# Se o resultado anterior for maior que 9:
#     resultado é 0
# contrário disso:
#     resultado é o valor da conta

# O segundo dígito do CPF é 0

cpf_entrada = '746.824.890-70'
cpf = cpf_entrada.replace('.' or '-','')[:9]
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

digito_cpf_entrada = cpf_entrada.split('-')[1]
digito_cpf = str(primeiro_digito) + str(segundo_digito)

if digito_cpf == digito_cpf_entrada:
    print('CPF Válido')
else:
    print('CPF Inválido')