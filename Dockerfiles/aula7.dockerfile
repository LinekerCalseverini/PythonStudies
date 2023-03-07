FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula7 .

RUN chmod -R o+rx ./

CMD ["python3", "aula7.py"]
