# Argumentos nomeados e não nomeados em funções Python
# Argumento nomeado tem nome com sinal de igual
# Argumento não nomeado recebe apenas o argumento (valor)

# Variável na definição = parâmetro
# Variável na chamada da função = argumento

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)

soma(1, 2, 3)

# Use argumentos nomeados apenas APÓS argumentos posicionais
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')