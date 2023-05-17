import requests
from pprint import pprint
from pathlib import Path

WORKDIR = Path(__file__).parent
TOKEN_FILE = WORKDIR / 'token.txt'

_print = print
print = pprint

url = 'http://localhost:3001/tokens'

user_data = dict(password='123456',
                 email='luiz@email.com')

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)
    response_data = response.json()
    token = response_data.get('token')

    with open(TOKEN_FILE, 'w') as f:
        f.write(token)

    # print('Bytes', response.content)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
    # print('Bytes', response.content)
