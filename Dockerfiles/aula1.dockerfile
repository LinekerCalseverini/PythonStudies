FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY . .

CMD ["python3","aula1.py"]
