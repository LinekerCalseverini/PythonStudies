#!/usr/local/bin/python3
# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('')

if not senha:
    if senha == '123456':
        print('Entrou')
    else:
        print('Senha incorreta.')

print(not 0) # = True
print(not 1) # = False