FROM python:slim

WORKDIR /

COPY . /

RUN pip install -r requirement.txt

EXPOSE 8000

CMD python manage.py runserver