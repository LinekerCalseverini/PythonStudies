# Context Manager com fnção - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager
from pathlib import Path
main_dir = Path('.') / 'Aula150'

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open(main_dir / 'aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n', 123)
    arquivo.write('Linha 1\n')
    print('WITH', arquivo)