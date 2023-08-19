FROM python:3.9

RUN useradd -d /home/inge/ -m -p inge inge

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY . /app

RUN chmod -R a-w /app

USER inge


EXPOSE 5000

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]

