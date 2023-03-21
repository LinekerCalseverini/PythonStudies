# enumerate - enumera iteráveis (índices)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')

#     for valor in tupla_enumerada:
#         print(f'\t{valor}')