# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

def escolher_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = escolher_multiplicador(2)
triplicar = escolher_multiplicador(3)
quadruplicar = escolher_multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))
