# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor = 1_000_000
data_emprestimo = datetime.strptime('20/12/2020', '%d/%m/%Y')
data_final = data_emprestimo + relativedelta(years=5)
data_parcela = data_emprestimo + relativedelta(months=1)
counter = 0

while data_parcela <= data_final:
    print(data_parcela.strftime('%d/%m/%Y'))
    data_parcela += relativedelta(months=1)
    counter += 1

print(f'{counter}x de R${valor/counter:,.2f}')
