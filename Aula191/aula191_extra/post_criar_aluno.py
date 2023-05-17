import requests
from pprint import pprint
from pathlib import Path
from get_token import token

WORKDIR = Path(__file__).parent
TOKEN_FILE = WORKDIR / 'token.txt'

_print = print
print = pprint

url = 'http://localhost:3001/alunos'

headers = dict(
    Authorization=token
)

aluno_data = dict(
    nome='Luana2',
    sobrenome='Vieira',
    email='luana2@email.com',
    idade=50,
    peso=80.04,
    altura=1.90
)

response = requests.post(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)
    response_data = response.json()
    print(response_data)

    # print('Bytes', response.content)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
    # print('Bytes', response.content)
