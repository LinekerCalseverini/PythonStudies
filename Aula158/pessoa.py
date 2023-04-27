from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int) -> None:
        if not isinstance(nome, str):
            raise TypeError('nome must be string')

        if not isinstance(idade, int):
            raise TypeError('idade must be int')

        self._nome = nome
        self._idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise TypeError('nome must be string')

        self._nome = nome

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: int) -> None:
        if not isinstance(idade, int):
            raise TypeError('idade must be int')

        self._idade = idade
