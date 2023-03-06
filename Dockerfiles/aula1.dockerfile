FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula1 .

CMD ["python3","aula1.py"]
