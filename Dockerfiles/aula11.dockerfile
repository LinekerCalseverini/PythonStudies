FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula11 .

RUN chmod -R +x ./

CMD ["python3", "aula11.py"]
