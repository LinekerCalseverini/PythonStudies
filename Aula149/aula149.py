# Context Manager com classes
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato
# Para criar um context, manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e
# traceback. Se ele retornar True, exceção no with serão
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...
class MyContextManager:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo

    def __enter__(self):
        return open(self.caminho_arquivo, self.modo)
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('EXIT')

instancia = MyContextManager('aula149.txt', 'w')

with instancia as alguma_coisa:
    print('WITH', alguma_coisa)