from dataclasses import dataclass, field


class OldPerson:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname: str = firstname
        self.lastname: str = lastname

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.firstname} {self.lastname})'

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __value: object) -> bool:
        return str(self) == str(__value)


@dataclass(frozen=True, kw_only=True, slots=True)
class Person:
    firstname: str
    lastname: str
    active: bool = False
    addresses: list = field(
        default_factory=list, repr=False, compare=True, kw_only=True
    )
    full_name: str = field(default='Missing', init=False, repr=False)

    def __post_init__(self) -> None:
        full_name = f'{self.firstname} {self.lastname}'
        object.__setattr__(self, 'full_name', full_name)

    def get_full_name(self) -> str:
        return self.full_name

    @property
    def p_full_name(self) -> str:
        return self.full_name


if __name__ == '__main__':
    john1 = Person(firstname='John', lastname='Doe',
                   active=True, addresses=['R1'])
    john2 = Person(firstname='John', lastname='Doe',
                   active=True, addresses=['R2'])
    # john1.active = True
    print(john1.get_full_name())
    print(john2.p_full_name)
