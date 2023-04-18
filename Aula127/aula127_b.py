# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
from aula127_a import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO) as arquivo:
    pessoas = json.load(arquivo)

pessoas = [
    Pessoa(**pessoa)
    for pessoa in pessoas
]

for pessoa in pessoas:
    print(pessoa.nome)

print(__name__)