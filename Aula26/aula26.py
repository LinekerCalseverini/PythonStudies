#!/usr/bin/local/python3
# Interpolação básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x e X - Hexadecimal (0123456789ABCDEF)
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal - + ou -
# = - Força números a aparecer após o sinal
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a
# !r = __repr__
# !s = __str__
# !a = __asc__

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # =        ABC
print(f'{variavel: <10}') # = ABC       
print(f'{variavel: ^10}') # =    ABC    
print(f'{1000.4873648123746:0=+10,.1f}') # = +001,000.5
print(f'O hexadecimal de 1500 é {1500:08x}') # = 000005DC
print(f'{variavel!r}')