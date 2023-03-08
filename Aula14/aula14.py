#!/usr/local/bin/python3
a = 'AAAAA'
b = 'BBBBB'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

# Também é possível passar por índices
string = 'b={1} a={0} a={0} a={0} c={2:.2f}'
formato = string.format(a, b, c)

# Com parâmetros nomeados
string = 'b={nome2} a={nome1} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)