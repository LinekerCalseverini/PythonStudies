FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula28 .

RUN chmod -R +x ./

CMD ["python3", "aula28.py"]
