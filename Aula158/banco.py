from conta_banco import Conta
from cliente import Cliente


class Banco:
    def __init__(self) -> None:
        self._clientes: set[Cliente] = set()

    def adicionar_conta(self, cliente: Cliente, conta: Conta) -> None:
        if not isinstance(conta, Conta):
            raise TypeError('Cannot add non-Conta type to list')

        cliente.contas.append(conta)
        self._clientes.add(cliente)

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self):
        raise AttributeError('Cannot change client list')

    def listar_clientes(self) -> None:
        for cliente in self.clientes:
            print(cliente)
