FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3
RUN apt-get install -y python3-pymysql
RUN apt-get install -y python3-flask
RUN apt-get install -y python-boto3


copy . .

EXPOSE 80

CMD ["python3", "EmpApp.py"]
