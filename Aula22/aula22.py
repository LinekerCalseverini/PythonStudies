#!/usr/local/bin/python3
# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input("Entrada: ")
senha_permitida = '123456'

# if True:
# ...

# Não é necessário testar se é maiúscula ou minúscula, usar string.upper() para tornar sempre maiúscula
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
     print('Sair')

# Avaliação de curto circuito:
print(True and False and True)
#              ^ Vai parar aqui

print(True and 0 and True)
#              ^ Vai parar aqui

print(True or False or 0 or 'abc' or True)
#     ^ Vai parar aqui