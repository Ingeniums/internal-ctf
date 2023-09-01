
FROM python:3.9

RUN apt-get update && \
    apt-get install -y npm  && \
    rm -rf /var/lib/apt/lists/*



RUN useradd -d /home/inge/ -m -p inge inge
WORKDIR /challenge

COPY ./requirement.txt requirement.txt

RUN python -m pip install -r requirement.txt

COPY . /challenge


RUN npm install -D tailwindcss
RUN npx tailwindcss init 

COPY flag.txt /flag

RUN chmod -R a-w /challenge
RUN chmod a+w /challenge/uploads

USER inge

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
