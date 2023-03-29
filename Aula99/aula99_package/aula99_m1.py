# Para limitar a quantidade de funções que o import * puxa, você pode usar o
# atributo __all__, e você deve passar uma lista de strings contendo os nomes
# # de atributos e métodos
# __all__ = [
#     'variavel'
# ]
from aula99_package.aula99_m2 import fala_oi

def soma_do_modulo(x,y):
    return x+y

variavel = 'Alguma coisa'
nova_variavel = 'OK'

fala_oi()