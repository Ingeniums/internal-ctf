#!/bin/bash 


while :; do
    echo "echo 'ingeniums{n3v3r_Wr1te_p455W0rd_pl41n_txt_1n_t3rmin4l}'" >> /home/4dm1n/.bash_history
    echo "echo 'Ooh Well done, ~!@#$%^&**)_+'" >> /home/inge/.bash_history
    echo 'su 4dm1n --password h0pefu11yUn6ue$$abl3' >> /home/inge/.bash_history
    socat -dd -T60 tcp-l:1025,reuseaddr,fork,su=inge exec:'bash -i',pty,stderr
done
