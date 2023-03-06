FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula4 .

CMD ["python3", "./aula4.py"]

