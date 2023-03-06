FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula6 .

CMD ["chmod -R o+rx ./"]

CMD ["python3", "./aula6.py"]