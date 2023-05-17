import requests
from pprint import pprint
from pathlib import Path
from get_token import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

_print = print
print = pprint

WORKDIR = Path(__file__).parent
TOKEN_FILE = WORKDIR / 'token.txt'
mimetypes = MimeTypes()

nome_arquivo = WORKDIR / 'foto.jpg'
mimetype_arquivo = mimetypes.guess_type(nome_arquivo)[0]

multipart = MultipartEncoder(fields={
    'aluno_id': '2',
    'foto': (nome_arquivo, open(nome_arquivo, 'rb'), mimetype_arquivo)
})

url = 'http://localhost:3001/fotos'

headers: dict = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.put(url=url, headers=headers)

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
