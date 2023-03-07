#!/usr/local/bin/python3
# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão
# Python usa snake_case (tudo minúsculo com separação em _)

nome_completo = 'Luiz Otávio Miranda'
soma_dois_mais_dois = 2 + 2
int_um = bool('1')
print(int_um, type(int_um))
print(nome_completo, soma_dois_mais_dois) # Luiz Otávio Miranda 4

nome = 'Luiz'
idade = 30
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)

# Praticando f-strings, não faz parte da aula
print(f'Nome: {nome}\nIdade: {idade}\nÉ maior? {maior_de_idade}')

# Praticando if conditions, não faz parte da aula
print(f'Nome: {nome}\nIdade: {idade}')
print('É maior?', end=' ')
if maior_de_idade:
    print('Sim')
else:
    print('Não')

