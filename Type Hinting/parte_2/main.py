# uma_string: str = 'Um valor'
# um_inteiro: int = 123456
# um_float: float = 10.5
# um_booleano: bool = True
# uma_lista: list = [1, 2, 3]
# uma_tupla: tuple = (1, 2, 3)
# um_conjunto: set = {1, 2, 3}
# um_dicionario: dict = {'nome': 'Luiz', 'sobrenome': 'Miranda'}

# def soma(x: int, y: int, z: float) -> float:
#     return x + y + z

# lista_inteiros: list[int] = [1, 2, 3, 4]
# lista_strings: list[str] = ['a', 'b', 'c', 'd']
# lista_tuplas: list[tuple] = [(1, 'a'), (2, 'b')]
# lista_listas_int: list[list[int]] = [[1], [4, 5]]

# um_dict: dict[str, int] = {
#     'A': 0,
#     'B': 0,
#     'C': 0,
# }

# um_dict_de_listas: dict[str, list[int]] = {
#     'A': [1, 2],
#     'B': [3, 4],
#     'C': [5, 6],
# }

# um_set_de_inteiros: set[int] = {1, 2, 3}

# ListaInteiros = list[int]  # Type alias
# DictListaInteiros = dict[str, ListaInteiros]

# um_dict_de_listas: DictListaInteiros = {
#     'A': [1, 2],
#     'B': [3, 4],
#     'C': [5, 6],
# }

# string_e_inteiros: int | str = 1  # Union
# string_e_inteiros = 'A'  # Sem erros
# string_e_inteiros = 2  # Sem erros
# lista_inteiros: list[int | str] = [1, 2, 3, 4, 'a']

# def soma(x: int, y: float | None = None) -> float:
#     if isinstance(y, float | int):
#         return x + y

#     return x
# from typing import Callable

# SomaInteiros = Callable[[int, int], int]


# def executa(func: SomaInteiros, a: int, b: int) -> int:
#     return func(a, b)


# def soma(x: int, y: int) -> int:
#     return x + y


# print(executa(soma, 1, 10))
# from typing import TypeVar

# T = TypeVar('T')


# def get_item(lista: list[T], index: int) -> T:
#     return lista[index]


# list_item = get_item([1, 2, 3], 1)  # int
# list_str = get_item(['a', 'b', 'c'], 1)  # str
# class Person:
#     def __init__(self, firstname: str, lastname: str) -> None:
#         self.firstname: str = firstname
#         self.lastname: str = lastname

#     @property
#     def full_name(self) -> str:
#         return f'{self.firstname} {self.lastname}'


# def say_my_name(person: Person) -> str:
#     return person.full_name


# print(say_my_name(Person('John', 'Doe')))
