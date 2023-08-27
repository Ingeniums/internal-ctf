FROM python:3.9

RUN useradd -d /home/inge/ -m -p inge inge

WORKDIR /challenge

COPY ./requirement.txt requirement.txt

RUN python -m pip install -r requirement.txt

COPY . /challenge

RUN chmod -R a-w /challenge

USER 1000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5001

CMD ["flask", "run"]
