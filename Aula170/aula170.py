# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# para fins didáticos, vou usar o caminho ./Aula170
import os

caminho = os.path.join('.', 'Aula170')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print(imagem)
