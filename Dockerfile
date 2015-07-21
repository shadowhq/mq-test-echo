FROM python:2.7
ENV MQ_HOST shadow-rabbitmq

ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt
ENTRYPOINT python src/main.py