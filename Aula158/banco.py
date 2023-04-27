from conta_banco import Conta
from cliente import Cliente

class Banco:
    _clientes = set()
    
    @classmethod
    def adicionar_conta(cls, cliente: Cliente, conta: Conta) -> None:
        if not isinstance(conta, Conta):
            raise TypeError('Cannot add non-Conta type to list')

        cliente.contas.append(conta)
        cls._clientes.add(cliente)

    @property
    @classmethod
    def clientes(cls):
        return cls._clientes

    @clientes.setter
    @classmethod
    def clientes(cls, *args, **kwargs):
        raise AttributeError('Cannot change client list')

    @classmethod
    def listar_clientes(cls):
        for cliente in cls._clientes:
            print(cliente)