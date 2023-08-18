FROM pwn.red/jail

ENV JAIL_PORT=1338

COPY --from=ubuntu / /srv
COPY ./challenge/chal /srv/app/run
COPY ./challenge/libc.so.6 /srv/app/
COPY ./challenge/ld-2.35.so /srv/app/

COPY flag.txt /srv/app/flag.txt

RUN chmod 755 /srv/app/run
