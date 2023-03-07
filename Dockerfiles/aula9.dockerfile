FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula9 .

RUN chmod +x ./

CMD ["python3", "aula9.py"]
