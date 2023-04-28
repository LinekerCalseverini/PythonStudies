# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = './Aula127/aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 16)
p2 = Pessoa('Maria', 19)
p3 = Pessoa('Cláudia', 23)
bd = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    print('FAZENDO DUMP')
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo)

if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()

print(__name__)