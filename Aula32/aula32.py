# Exercícios
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
print('{:-^30}'.format('Exercício 1'))
numero = input('Digite um número: ')
try:
    numero = int(numero)
    if numero % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar.')
except ValueError:
    print('Este não é um número.')

# Fala um programa que pergunte a hora ao usuário e, baseandose- no horário
# descrito, exiba a saudação apropriedada. Ex:
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
print('{:-^30}'.format('Exercício 2'))
hora = input('Digite a hora atual, de 0 a 23: ')
try:
    hora = int(hora)
    if hora >= 0 and hora <=23:
        if hora >= 0 and hora < 12:
            print('Bom dia')
        elif hora >= 12 and hora < 18:
            print('Boa tarde')
        else:
            print('Boa noite')
    else:
        print('Você não digitou um valor de 0 a 23.')
except ValueError:
    print('Você não digitou um valor de 0 a 23.')

# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
# menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
# "Seu nome é normal"; maior que 6, escreva "Seu nome é muito grande".
print('{:-^30}'.format('Exercício 3'))
nome = input('Digite o seu primeiro nome: ')
qtd_letras = len(nome)

if qtd_letras <= 4:
    print('Seu nome é curto')
elif qtd_letras > 4 and qtd_letras <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
