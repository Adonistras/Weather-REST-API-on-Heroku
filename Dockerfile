FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /home/adonistras/app/WeatherAPP

COPY ./requirements.txt /home/adonistras/app/WeatherAPP/requirements.txt

RUN pip install -r /home/adonistras/app/WeatherAPP/requirements.txt

COPY . /home/adonistras/app/WeatherAPP

EXPOSE 8000