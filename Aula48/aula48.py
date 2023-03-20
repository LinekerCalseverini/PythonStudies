# Listas em Python
# Similar a Array ou Vetor
# Tipo list = Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +
# Create Read Update Delete
# Criar, ler, alterar, apagar = lista [i] (CRUD)

lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append('BBB')
ultimo_valor = lista.pop(3)
print(lista, 'Removido,',ultimo_valor)
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]

lista.insert(3,5)
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

# Cuidados com dados mutáveis
# = - copiado o valor (imutáveis)
# = - aponta para o mesmo valor na memória (mutável)

# nome = 'Luiz'
# noutra_variavel = nome
# nome = 'João'
# print(nome)
# print(noutra_variavel)

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # Terão o mesmo endereço de memória

lista_a.insert(0,'Qualquer coisa')
print(lista_b)
