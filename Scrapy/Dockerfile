# Version: 0.0.1

FROM python:2

COPY . /home/cesar/webscraping/Scrapy/

WORKDIR /home/cesar/webscraping/Scrapy/

RUN virtualenv -p /usr/bin/python2.7 .

RUN ls -a

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

RUN pip install scrapy

RUN pip install pillow

RUN ls -a

WORKDIR /home/cesar/webscraping/Scrapy/movistar/

RUN ls

CMD scrapy crawl movistar -t csv

