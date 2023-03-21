# Faça uma lista de comprar com listas
# O usuário deve ter a possibilidade de
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com
# erros de índicess inexistentes na lista.

import os
lista_compras = []
listar = None

while True:
    os.system('cls')
    print('{:-^30}'.format('Lista de Compras'))
    if listar:
        for indice, item in enumerate(lista_compras):
            print(f'{indice} - {item:<15}')
        listar = False
    opcao = input('[I]nserir | [A]pagar | [L]istar: ')

    if len(opcao) > 1:
        print('Digite apenas a letra inicial')
    elif opcao.upper() == 'I':
        item = input('Que item deseja inserir? ')
        lista_compras.append(item)
    elif opcao.upper() == 'A':
        indice = input('Qual índice da lista deseja apagar? ')
        try:
            lista_compras.pop(int(indice))
        except ValueError:
            print('O índice deve ser um número inteiro.')
            input()
        except IndexError:
            print('Índice não encontrado na lista.')
            input()
        except:
            print('Erro inesperado.')
            input()
    elif opcao.upper() == 'L':
        listar = True
    else:
        print('Opção inválida.')
        input()