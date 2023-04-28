# # Aula 76
# * Dicionários em Python (tipo dict)
# * Dicionários são estruturas de dados do tipo
# *     par de "chave" e "valor".
# * Chaves podem ser consideradas como o "índice"
# *     que vimos na lista e podem ser de tipos imutáveis
# *     como: str, int, float, bool, tuple, etc.
# * O valor pode ser de qualquer tipo, incluindo outro
# *     dicionário.
# * Usamos as chaves - {} - ou a classe dict para criar
# *     dicionários.
# * Imutáveis: str, int, float, bool, tuple
# * Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321}
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

# ! Criei essa função recursiva para imprimir todas as chaves valores como string
# !     na tela
# def imprimirDicionario(dicionario):
#     def desempacotarListaDicionario(lista):
#         for item in lista:
#             imprimirDicionario(item)

#     for chave in dicionario:
#         if type(dicionario[chave]) == list:
#             desempacotarListaDicionario(dicionario[chave])
#         else:
#             print(f'{chave.capitalize()}: {dicionario[chave]}')

# * Como criar um dicionário
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321}
#     ]
# }

# imprimirDicionario(pessoa)

# * CRUD do Dicionário em Python
# pessoa = {}
# chave = 'nome_completo'
# pessoa[chave] = 'Luiz Otávio'
# pessoa['sobrenome'] = 'Miranda'
# lista = []

# print(pessoa[chave])
# pessoa[chave] = 'Maria'
# del pessoa['sobrenome']

# if pessoa.get('sobrenome') is not None:
#     print(pessoa['sobrenome'])

# * Métodos úteis dos dicionários em Python
# * len - quantas chaves
# * keys - iterável com as chaves
# * values - iterável com os valores
# * items - iterável com chaves e valores
# * setdefault - adiciona valor se a chave não existe
# * copy - retorna uma cópia rasa (shallow copy)
# * get - obtém uma chave
# * pop - Apaga um item com a chave especificada (del)
# * popitem - Apaga o último item adicionado
# * update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda'
}
# print(p1.get('nome', 'Não existe'))
# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'),('idade', 30))
# p1.update(tupla)
# print(p1)
# lista = [['nome', 'novo valor'],['idade', 30]]
# p1.update(lista)
# print(p1)

# ! Módulo de Python com métodos de hard copy
# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2]
# }
# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 999999
# print(d1)
# print(d2)

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 900
# }

# pessoa.setdefault('idade', 0)
# print(pessoa.get('idade'))

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.items():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)