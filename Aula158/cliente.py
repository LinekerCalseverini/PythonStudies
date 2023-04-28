from pessoa import Pessoa
from conta_banco import InvalidAccountOperationError


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self._contas: list[Cliente] = []

    @property
    def contas(self) -> list:
        return self._contas

    @contas.setter
    def contas(self, *args, **kwargs) -> None:
        raise InvalidAccountOperationError('Cannot change account list')

    def __str__(self):
        nome = f'Cliente: {self._nome}'
        idade = f'Idade: {self._idade}'
        contas = ''
        for conta in self._contas:
            contas += f'{conta}\n\n'
        return f'--------------------------------------\n' \
               f'{nome}\n{idade}\n\n{contas}' \
               f'--------------------------------------\n'
