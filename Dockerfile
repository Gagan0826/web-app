FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN pip3 install pymysql flask boto3

COPY . .

EXPOSE 80

CMD ["python3", "EmpApp.py"]
