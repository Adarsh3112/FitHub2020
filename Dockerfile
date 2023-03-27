FROM python:3.9-slim-buster

WORKDIR /
# RUN mkdir build && python manage.py collectstatic
COPY . /

RUN pip install -r requirement.txt

EXPOSE 8000

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000