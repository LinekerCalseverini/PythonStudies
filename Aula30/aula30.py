# CONSTANTE = "Variáveis" que não vão mudar
# Python não existe um conceito de variáveis constantes, mas a convenção é que constantes estejam todas em maiúsculo

# Muitas condições no mesmo if (ruim) - evitar muitas condições de if

#    <- Contagem de complexidade (ruim) - Se houver muitos tabs seguidos de identação, é difícil de se ler o código

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

    if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE):
        print('carro multado em radar 1')