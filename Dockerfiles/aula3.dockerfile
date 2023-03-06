FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula3 .

CMD ["python3","aula3.py"]

