FROM python:3.7-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . /app

WORKDIR /app

CMD ["python3", "salary/manage.py", "runserver", "0:8000"]
# CMD python3 manage.py migrate && python3 manage.py loaddata ingredients.json && gunicorn foodgram.wsgi:application --bind 0:8000 