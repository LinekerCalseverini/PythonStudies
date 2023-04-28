# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou impar.
def resolverPar(numero):
    return 'Par' if numero % 2 == 0 else 'Ímpar'

print(multiplicar(1, 2, 3, 4, 5))
print(resolverPar(7))
