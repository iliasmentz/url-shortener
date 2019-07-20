FROM ubuntu:18.10

LABEL Maintainer="Ilias Mentzelos <iliasmentz@gmail.com>"

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /shorty/requirements.txt

WORKDIR /shorty

RUN pip3 install -r requirements.txt

COPY . /shorty

ENTRYPOINT [ "python3" ]

CMD [ "run.py" ]