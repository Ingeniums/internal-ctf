# sudo docker build -t heap1 .
# sudo docker run -d -p 1024:1024 --rm -it heap1

FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y socat gcc && \
    rm -rf /var/lib/apt/lists/*


RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY chal.c .
COPY flag.txt .

RUN gcc chal.c -o elf -fstack-protector -Wl,-z,relro,-z,now -no-pie
RUN ldd ./elf
RUN chown -R root:root /home/ctf
RUN chmod +x ./elf

USER ctf
EXPOSE 1024

ENTRYPOINT socat TCP-LISTEN:1024,reuseaddr,fork EXEC:"./elf"