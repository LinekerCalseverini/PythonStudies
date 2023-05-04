# os + shutil - Copiando arquivos com Python
# 1 - Vamos copiar arquivos de uma pasta para outra.
# Mover/Renomear -> shutil.move
# Mover/Renomear -> os.rename
# Copiar -> shutil.copy
# Apagar -> os.unlink
# Apagar diretório recursivamente -> shutil.rmtree
import os
import shutil

# HOME = os.path.expanduser('~')
# DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ROOT = os.path.join('.', 'Aula173')
PASTA_ORIGINAL = os.path.join(PASTA_ROOT, 'PASTA_ANTIGA')
NOVA_PASTA = os.path.join(PASTA_ROOT, 'NOVA_PASTA')
# print(HOME)
# print(NOVA_PASTA)

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
