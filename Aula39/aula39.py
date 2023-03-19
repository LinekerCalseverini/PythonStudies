# Iterando strings com while

#       0123456789A
nome = 'Luiz Otávio' # Iteráveis
tamanho_nome = len(nome)
contador = 0
nova_string = ''

while contador < tamanho_nome:
    nova_string += f'*{nome[contador]}'
    contador += 1

nova_string += '*'
print(nova_string)