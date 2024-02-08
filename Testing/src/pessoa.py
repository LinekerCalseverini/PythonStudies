import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get('www.exemplo.com')

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'

        self.dados_obtidos = False
        return 'ERRO 404'
