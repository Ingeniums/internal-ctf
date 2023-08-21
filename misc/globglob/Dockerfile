FROM python:slim AS app

FROM pwn.red/jail
COPY --from=app / /srv
COPY app.py /srv/app/run
COPY flag.txt /srv/app/

ENV JAIL_PORT=1234
