FROM ubuntu:16.04
MAINTAINER Cody Chan "int64ago@gmail.com"

RUN sed -i 's/archive\.ubuntu\.com/mirrors\.163\.com/g' /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]