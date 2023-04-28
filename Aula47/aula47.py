# Faça um jogo para o usuário adivinhar qual
# a palavra secreta.
# - Você vai propor uma palavra secreta
# qualquer e vai dar a possibilidade para
# o usuário digitar apenas uma letra.
# - Quando o usuário digitar uma letra, você
# vai conferir se a letra digitada está
# na palavra secreta.
#       - Se a letra digitada estiver na
#       palavra secreta; exiba a letra;
#       - Se a letra digitada não estiver
#       na palavra secreta; exiba *.
# Faça a contagem de tentativas do seu
# usuário.

# print('{:-^30}'.format('Exercício: Palavra Secreta'))
# palavra_secreta = 'perfume'
# palavra_revelada = '*******'
# jogo_iniciado = True
# tentativas = 0

# while jogo_iniciado:
#     chute = input('Digite uma letra: ')

#     if len(chute) > 1:
#         print('Digite apenas uma letra.')
#         tentativas += 1
#         continue

#     if chute.isdigit():
#         print('Digite um caracter alfabético.')
#         tentativas += 1
#         continue
    
#     if chute in palavra_secreta:
#         i = 0
#         while i < len(palavra_revelada):
#             try:
#                 if chute == palavra_secreta[i]:
#                     palavra_revelada = f'{palavra_revelada[0:i]}{chute}'\
#                                        f'{palavra_revelada[i+1:]}'
#             except IndexError:
#                 palavra_revelada = f'{palavra_revelada[0:i]}{chute}'
#                 break
#             i += 1
    
#     print(palavra_revelada)
#     tentativas += 1
#     jogo_iniciado = palavra_revelada != palavra_secreta

# print(f'Parabéns, você levou {tentativas} tentativas para acertar.')

# Solução do professor
import os

print('{:-^30}'.format('Exercício: Palavra Secreta'))
palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0
jogo_iniciado = True

while jogo_iniciado:
    chute = input('Digite uma letra: ')
    if len(chute) > 1:
        print('Digite apenas uma letra.')
        tentativas += 1
        continue

    if chute.isdigit():
        print('Digite um caracter alfabético.')
        tentativas += 1
        continue
    
    if chute in palavra_secreta:
        letras_acertadas += chute
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    jogo_iniciado = palavra_formada != palavra_secreta

    print(palavra_formada)
    input()
    os.system('cls')
    tentativas += 1
else:
    print(f'Parabéns, você levou {tentativas} tentativas para acertar.')