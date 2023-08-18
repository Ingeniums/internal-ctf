FROM python:3.9

RUN useradd -d /home/inge/ -m -p inge inge

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY . /app

RUN chmod -R a-w /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
