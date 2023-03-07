FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula8 .

RUN chmod +x ./

CMD ["python3", "aula8.py"]
