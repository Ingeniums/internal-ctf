FROM pwn.red/jail

ENV JAIL_PORT=1336

COPY --from=ubuntu / /srv
COPY ./challenge/duel /srv/app/run

COPY flag.txt /srv/app/flag.txt

RUN chmod 755 /srv/app/run
