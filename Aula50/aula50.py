# Exercício
# Exiba os índices da lista
# Maria
# Helena
# Luiz

lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(lista.index(nome), nome, type(nome))

# Resolução do professor
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))