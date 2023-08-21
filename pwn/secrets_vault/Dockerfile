FROM pwn.red/jail

ENV JAIL_PORT=1335

COPY --from=ubuntu / /srv
COPY ./challenge/chal_patched /srv/app/run
COPY ./challenge/ld.so.2 /srv/app/
COPY ./challenge/libc.so.6 /srv/app/
COPY flag.txt /srv/app/flag.txt

RUN chmod 755 /srv/app/run
