# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizone', 'MG')]

def zipper(lista1, lista2):
    lista_unida = []
    if len(lista1) <= len(lista2):
        lista_menor = lista1
        lista_maior = lista2
    else:
        lista_menor = lista2
        lista_maior = lista1

    for i in range(len(lista_menor)):
        lista_unida.append((lista_menor[i], lista_maior[i]))
    return lista_unida

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

cidades_estados = zipper(cidades, estados)

print(cidades_estados)