FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula5 .

CMD ["python3", "./aula5.py"]

