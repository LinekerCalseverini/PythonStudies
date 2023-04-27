from abc import ABC, abstractmethod


class InvalidAccountOperationError(Exception):
    pass


class Conta(ABC):
    def __init__(self,
                 agencia: str,
                 numero_conta: str,
                 saldo: float = 0.0) -> None:
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @abstractmethod
    def depositar(self, quantia: float) -> None: ...

    @abstractmethod
    def sacar(self, quantia: float) -> None: ...

    @property
    def agencia(self) -> str:
        return self._agencia

    @agencia.setter
    def agencia(self, *args, **kwargs) -> None:
        raise InvalidAccountOperationError(
            'Impossível alterar a agência de uma conta'
            )

    @property
    def numero_conta(self) -> str:
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, *args, **kwargs) -> None:
        raise InvalidAccountOperationError(
            'Impossível alterar o número de uma conta'
            )

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, *args, **kwargs) -> None:
        raise InvalidAccountOperationError(
            'Impossível alterar o saldo diretamente'
            )

    def mostrar_saldo(self):
        if self.saldo < 0:
            return f'-R${abs(self.saldo):,.2f}'

        return f'R${self.saldo:,.2f}'

    def __str__(self):
        return f'Agência: {self.agencia}\nConta: {self.numero_conta}\n' \
               f'Saldo: {self.mostrar_saldo()}'


class ContaCorrente(Conta):
    def __init__(self,
                 agencia: str,
                 numero_conta: str,
                 saldo: float,
                 limite: float = 0) -> None:
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite: float):
        self._limite = limite

    def depositar(self, quantia: float) -> None:
        self._saldo += quantia

    def sacar(self, quantia: float) -> None:
        if quantia > self._saldo + self._limite:
            print('Saldo insuficiente')
            return

        self._saldo -= quantia

    def __str__(self):
        return f'{super().__str__()}\nLimite: R${self.limite:,.2f}'


class ContaPoupanca(Conta):
    def depositar(self, quantia: float) -> None:
        self._saldo += quantia

    def sacar(self, quantia: float) -> None:
        if quantia > self._saldo:
            print('Saldo insuficiente')
            return

        self._saldo -= quantia
