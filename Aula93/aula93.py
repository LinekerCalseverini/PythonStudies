# Try, except, else e finally
string = 'Luiz'
print(isinstance(string,str))

a = 18
b = None
try:
    print('Linha 1')
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Divisão por zero')
except (NameError, TypeError) as e:
    print('Não houve definição correta de \'b\'')
    print('TIPO: ', e.__class__.__name__)
    print('MSG: ', e)