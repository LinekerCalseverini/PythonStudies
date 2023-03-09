FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY ./Aula15 .

RUN chmod -R +x ./

RUN apk update

RUN apk add tzdata

RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

RUN echo "America/Sao_Paulo" >  /etc/timezone

ENV TZ America/Sao_Paulo

ENV LANG pt_BR.UTF-8

ENV LANGUAGE pt_BR.UTF-8

ENV LC_ALL pt_BR.UTF-8

CMD ["python3","aula15.py"]
