# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo, : dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass
# from dataclasses import asdict, astuple
from dataclasses import field
# from dataclasses import fields

# Parâmetro init: True = Cria __init__ / False = Não cria __init__
#     Se o init for False, o decorator não cria o __post_init__
# Parâmetro frozen: True = Parece o atributo "Final" do Java
# Parâmetro repr: True = cria __repr__ / False = não cria __repr__
# Parâmetro order: ativa organização da classe se existir uma lista de objetos
#     daquela classe


@dataclass(order=True)
class Pessoa:
    nome: str = field(
        default='MISSING'
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     print('POST INIT')

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)

    # p1 = Pessoa('Luiz', 'Otávio')
    # print(asdict(p1).keys())
    # print(asdict(p1).values())
    # print(asdict(p1).items())
    # print(astuple(p1)[0])

    # lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    # print(ordenadas)
