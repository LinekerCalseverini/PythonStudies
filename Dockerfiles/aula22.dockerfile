FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula22 .

RUN chmod -R +x ./

CMD ["python3", "aula22.py"]