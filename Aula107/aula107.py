# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizone', 'MG')]

# def zipper(lista1, lista2):
#     intervalo = min(len(lista1),len(lista2))
#     return [(lista1[i],lista2[i])
#             for i in range(intervalo)
#     ]

# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados = ['BA', 'SP', 'MG', 'RJ']

# cidades_estados = zipper(cidades, estados)

# print(cidades_estados)
from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(cidades,estados)))
print(list(zip_longest(cidades,estados, fillvalue='SEM CIDADE')))