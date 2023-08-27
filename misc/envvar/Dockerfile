FROM ubuntu:latest

 
RUN apt-get update && \
    apt-get install -y socat  && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash inge
RUN echo 'inge:inge' | chpasswd
#ENV  FLAG=ingeniums{$h3lL_Env1r3m3nT_Var1AbL3}
ENV FLAG=aW5nZW5pdW1zeyRoM2xMX0VudjFyM20zblRfVmFyMUFiTDN9
USER inge
EXPOSE 1030

ENTRYPOINT bash -c "socat -v tcp-listen:1030,reuseaddr,fork,keepalive EXEC:'bash -i',stderr"
