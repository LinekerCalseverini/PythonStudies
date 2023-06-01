# PyPDF2 - Para manipular arquivos PDF
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))

# for page in reader.pages:
#     print(page)

page_0 = reader.pages[0]
image_0 = page_0.images[0]

# print(page_0.extract_text())
# with open(PASTA_NOVA / image_0.name, 'wb') as image:
#     image.write(image_0.data)

# writer = PdfWriter()
# writer.add_page(page_0)

# with open(PASTA_NOVA / 'page_0.pdf', 'wb') as f:
#     writer.write(f)

# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()
#     with open(PASTA_NOVA / f'page_{i}.pdf', 'wb') as f:
#         writer.add_page(page)
#         writer.write(f)


files = [
    PASTA_NOVA / f'page_{i}.pdf'
    for i in range(2)
]

merger = PdfMerger()
for file in files:
