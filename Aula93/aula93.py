# Try, except, else e finally
a = 18
b = None
try:
    print('Linha 1')
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Divisão por zero')
except (NameError, TypeError):
    print('Não houve definição de \'b\'')