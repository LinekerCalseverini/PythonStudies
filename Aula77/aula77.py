# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': {'a': '1','b': '3','c': '4','d': '5'},
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': {'a': '25','b': '55','c': '10','d': '51'},
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': {'a': '4','b': '5','c': '2','d': '1'},
        'Resposta': '5'
    }
]
acertos = 0
print('{:-^20}'.format('SHOW DO MILHÃO'))

for pergunta in perguntas:
    print(f'Pergunta: {pergunta.get("Pergunta")}\n')

    print('Opções')
    for letra, resposta in pergunta.get('Opções').items():
        print(f'{letra}) {resposta: <2}')
    print()

    alternativa = input('Digite a alternativa correta: ')
    if pergunta.get('Opções').get(alternativa) == pergunta.get('Resposta'):
        print('Você acertou!')
        acertos += 1
    else:
        print('Você errou!')

    print()

print(f'Você acertou {acertos}\nde {len(perguntas)} perguntas.')
