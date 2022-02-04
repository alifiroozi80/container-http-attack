FROM python:3

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y net-tools \
    && apt-get install -y iputils-ping \
    && apt-get install -y httping

#COPY requirements.txt ./

#RUN pip install ping3

COPY command.py .

CMD [ "python", "./command.py" ]
