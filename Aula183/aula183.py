# string.Template para substituir variáveis em textos
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
# import json
import locale
from datetime import datetime
from string import Template
from pathlib import Path

locale.setlocale(locale.LC_ALL, 'pt_BR')

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'


def converte_para_brl(numero: float | int) -> str:
    brl = 'R$' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

# print(json.dumps(dados, ensure_ascii=False, indent=2))


class MyTemplate(Template):
    delimiter = '%'


with open(CAMINHO_ARQUIVO) as arquivo:
    texto = arquivo.read()

template = MyTemplate(texto)
print(template.substitute(dados))
