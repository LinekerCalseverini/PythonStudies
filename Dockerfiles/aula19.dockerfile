FROM python:3.11.2-alpine.3.17

WORKDIR /app

COPY ./Aula19 .

RUN chmod -R +x ./

CMD ["python3", "aula19.py"]