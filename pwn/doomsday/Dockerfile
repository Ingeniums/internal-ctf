FROM pwn.red/jail

ENV JAIL_PORT=1341

COPY --from=ubuntu / /srv
COPY ./challenge/chal_patched /srv/app/run
COPY ./challenge/ld-linux-x86-64.so.2 /srv/app/
COPY ./challenge/libc.so.6 /srv/app/
COPY flag.txt /srv/app/flag.txt

RUN chmod 755 /srv/app/run
