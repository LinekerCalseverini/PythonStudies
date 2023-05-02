# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.pythn.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

data = datetime.now(timezone('Asia/Tokyo'))
print(data.timestamp())  # Isso está na base de dados
print(datetime.fromtimestamp(1683024930))

# * Meus Testes
# * data_str = datetime.fromtimestamp(1683024930)
# * data = datetime.strftime(data_str, '%d/%m/%Y %H:%M:%S')
# * print(data)


# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# print(data)

# data_str = '2022/04/20 07:49:23'
# data_str = '20/04/2022 07:49:23'
# data_fmt = '%d/%m/%Y %H:%M:%S'
# data = datetime.strptime(data_str, data_fmt)
