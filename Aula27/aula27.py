#!/usr/bin/local/python3
# Fatiamento de strings
# 012345678
# Olá mundo
#-987654321
# Fatiamento [i:f:p] [::]
# i - início: onde começar?
# f - fim: onde parar de fatiar?
# o interpretador não considera o caracter final
# p - passo: de quanto em quanto?
# Obs.: a função len retorna a qtd
# de caracteres da str
variavel = 'Olá mundo'
print(variavel[4:]) # = mund
print(variavel[:5]) # = Olá m
print(variavel[-8:-2]) # lá mun

# A função len retorna o comprimento da string
print(len(variavel)) # = 9

print(variavel[0:len(variavel):2]) # = Oámnd
print(variavel[::-1]) # = odnum álO