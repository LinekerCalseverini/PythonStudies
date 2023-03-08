FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula14 .

RUN chmod -R +x ./

CMD ["python3", "aula14.py"]
