# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricantes na tela
class Carro:
    def __init__(self, nome, fabricante):
        self._nome = nome
        self._motor = None
        self._fabricante = fabricante

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, nome):
        self._nome = nome
        self._carros_compativeis = []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def carros_compativeis(self):
        return self._carros_compativeis
    
    def inserir_carro_compativel(self, carro):
        self.carros_compativeis.append(carro)

    def listar_carros_compativeis(self):
        for carro in self.carros_compativeis:
            print(carro.nome)

class Fabricante:
    def __init__(self, nome):
        self._nome = nome
        self._modelos_produzidos = []

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def modelos_produzidos(self):
        return self._modelos_produzidos
    
    def inserir_modelo_produzido(self, carro):
        self.modelos_produzidos.append(carro)
    
    def listar_modelos_produzidos(self):
        for modelo in self.modelos_produzidos:
            print(modelo.nome)

fabricante = Fabricante('Volkswagen')
motor = Motor('2.0')
carro = Carro('Fox', fabricante)
fabricante.inserir_modelo_produzido(carro)
carro.motor = motor
motor.inserir_carro_compativel(carro)

print(carro.nome)
print(carro.fabricante.nome)
print(carro.motor.nome)

print(fabricante.nome)
for modelo in fabricante.modelos_produzidos:
    print(modelo.nome)

print(motor.nome)
for carro in motor.carros_compativeis:
    print(carro.nome)