FROM python:3.8

WORKDIR /exercise

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD  . .

CMD [ "python", "date-time.py" ]