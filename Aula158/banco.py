from conta_banco import Conta
from cliente import Cliente


class Banco:
    def __init__(self) -> None:
        self._clientes: set[Cliente] = set()
        self._agencias: set[str] = set(['0000'])

    def adicionar_conta(self, cliente: Cliente, conta: Conta) -> None:
        if not isinstance(conta, Conta):
            raise TypeError('Cannot add non-Conta type to list')

        if conta.agencia not in self.agencias:
            raise NameError('Agência não encontrada em nosso sistema')

        cliente.contas.append(conta)
        self._clientes.add(cliente)

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self):
        raise AttributeError('Cannot change client list')

    @property
    def agencias(self):
        return self._agencias

    @agencias.setter
    def agencias(self):
        raise AttributeError('Cannot change agency list')

    def listar_clientes(self, lista_cliente: list[Cliente] = []) -> None:
        if not isinstance(lista_cliente, list):
            raise TypeError('lista_cliente must be type list')

        if lista_cliente:
            if not isinstance(lista_cliente[0], Cliente):
                raise TypeError('lista_cliente must be list of type '
                                'Cliente')

            for cliente in lista_cliente:
                print(cliente)
            return

        for cliente in self.clientes:
            print(cliente)

    def buscar_clientes(self, nome_cliente: str) -> None:
        if not isinstance(nome_cliente, str):
            raise TypeError('nome_cliente must be type str')

        busca = []
        for cliente in self.clientes:
            if nome_cliente in cliente.nome:
                busca.append(cliente)
        if busca:
            self.listar_clientes(busca)
            return
        print('Sua pesquisa por nome não retornou clientes')

    def buscar_agencia(self, agencia: str) -> None:
        if not isinstance(agencia, str):
            raise TypeError('agencia must be of type str')

        if agencia in self.agencias:
            print(f'Agência {agencia} encontrada')
            return

        print(f'Agência {agencia} não encontrada')

    def buscar_conta(self, numero_conta: str):
        if not isinstance(numero_conta, str):
            raise TypeError('numero_conta must be of type str')

        for cliente in self.clientes:
            for conta in cliente.contas:
                if conta.numero_conta == numero_conta:
                    print(f'Conta encontrada:\nCliente: {cliente.nome}'
                          f'\n{conta}')
