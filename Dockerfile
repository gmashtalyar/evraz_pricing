FROM python:3.11-slim

WORKDIR /app
RUN apt-get update && apt-get install -y curl && apt-get clean

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . /app/

CMD python3 manage.py makemigrations \
    && python3 manage.py migrate \
    && python3 manage.py collectstatic --no-input \
    && gunicorn -w 3 EvrazPricing.wsgi:application --bind 0.0.0.0:8000

