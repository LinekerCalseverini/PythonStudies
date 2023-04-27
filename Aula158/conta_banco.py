from abc import ABC, abstractmethod

class InvalidAccountOperationError(Exception):
    pass


class Conta(ABC):
    def __init__(self,
                 agencia: str,
                 numero_conta: str,
                 saldo: float = 0) -> None:
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = 0        
    
    @abstractmethod
    def depositar(self, quantia: float) -> None: ...

    @abstractmethod
    def sacar(self, quantia: float) -> None: ...

    @property
    def agencia(self) -> float:
        return self._agencia

    @agencia.setter
    def agencia(self, *args, **kwargs) -> None:
        raise InvalidAccountOperationError(
            'Impossível alterar a agência de uma conta'
            )

    @property        
    def numero_conta(self) -> float:
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

    def __str__(self):
        return f'Agência: {self.agencia}\nConta: {self.numero_conta}\n' \
               f'Saldo: {self.saldo}'


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
    def limite(self, limite):
        self._limite = limite

    def depositar(self, quantia: float) -> None:
        if self._limite < 0:
            self._limite = 0
            self._saldo += quantia - self._limite
        else:
            self._saldo += quantia

    def sacar(self, quantia: float) -> None:
        if quantia > self._saldo + self._limite:
            print('Saldo insuficiente')
        elif quantia > self._saldo:
            self._limite += self._saldo - quantia
            self._saldo = 0
        else:
            self._saldo -= quantia

    def __str__(self):
        return f'{super().__str__()}\nLimite: {self.limite}'


class ContaPoupanca(Conta):
    def depositar(self, quantia: float) -> None:
        self._saldo += quantia

    def sacar(self, quantia: float) -> None:
        if quantia > self._saldo:
            print('Saldo insuficiente')
        else:
            self._saldo -= quantia
