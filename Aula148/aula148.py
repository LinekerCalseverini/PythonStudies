# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗ DEVE retornar o novo objeto ❗
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗ NÃO DEVE retornar nada(None) ❗
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        # print('Antes de criar a instância')
        instancia = super().__new__(cls)
        # print('Depois de criar a instância')
        # instancia.x = 213
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return f'A()'

a = A()
# O procedimento acima internamente:
# a = object.__new__(A)
# a.__init__()
# print(a.x)