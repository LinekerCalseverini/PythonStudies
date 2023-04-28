# Higher Order Functions
# Funções de Primeira Classe

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

saudacao_2 = saudacao

print(
    executa(saudacao_2, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao_2, 'Boa noite', 'Maria')
)
