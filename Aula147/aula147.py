# Python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self, other) -  self < other
# __le__(self, other) -  self <= other
# __gt__(self, other) -  self > other
# __ge__(self, other) -  self >= other
# __eq__(self, other) -  self == other
# __ne__(self, other) -  self != other
# __add__(self, other) -  self + other
# __sub__(self, other) -  self - other
# __mul__(self, other) -  self * other
# __truediv__(self, other) -  self / other
# __neg__(self) -  -self
# __str__(self) -  str
# __repr__(self) -  str
class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'{self.x}, {self.y}'

    def __repr__(self) -> str:
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}()'

p1 = Ponto(1, 2)
p2 = Ponto(978, 976)
print(p1)
print(p2)