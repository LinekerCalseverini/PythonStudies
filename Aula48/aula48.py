# Listas em Python
# Similar a Array ou Vetor
# Tipo list = Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +

#        -54321
#         01234
string = 'ABCDE' # 5 caracteres
lista = []
# print(bool([])) = falsy

# Cada item da lista tem seu índice
lista = [123, True, 'Luiz Otávio', 1.2, []]
lista[-3] = 'Maria'

print(lista)
print(lista[2].upper(), type(lista[2]))