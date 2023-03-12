FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula20 .

RUN chmod -R +x ./

CMD ["python3","aula20.py"]