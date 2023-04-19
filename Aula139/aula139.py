# super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super().upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# string = MinhaString('Luiz')
# print(string.upper())
class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo
        
    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Ei, burlei o sistema.')


    def metodo(self):
        super(B, self).metodo() # executa A.metodo(self)
        super(C, self).metodo() # executa B.metodo(self)
        # super().metodo() - faz a linha acima implicitamente
        print('C')

c = C('Atributo','Qualquer')
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()
# print(C.mro())