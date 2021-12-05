# server information
#NAME="Centos"
#VERSION="7 (Ootpa)"
# OpenVPN installer for Debian, Ubuntu, Fedora, CentOS, Arch Linux, Oracle Linux, Rocky Linux and AlmaLinux.

#ssh into the server

# update the packages
sudo yum update -y

#create a non-root(taka) user with sudo permission
sudo useradd -G sudo -m taka -s /bin/bash

#change the password of the created user
passwd taka

#copy public key to ~/.ssh/authorized_keys
ssh-copy-id key.pub taka@ip address

#configure sshd
sudo vi /etc/ssh/sshd_config

# change PasswordAuthentication yes to no
# change PermitRootLogin yes to no

# restart sshd
sudo systemctl restart sshd

#install and configure openvpn
sudo wget https://github.com/Nyr/openvpn-install/raw/master/openvpn-install.sh
sudo ./openvpn-install.sh

# Enter a name for the first client: taka (in this case)

# change owner
sudo chown taka taka.ovpn

#Disable the logs
sudo vi /etc/openvpn/server/server.conf

#change verb 3 to 0

# restart openvpn server
sudo systemctl restart openvpn-server@server.service

#setup a MFA

#install google authenticator packeage
sudo yum install libpam-google-authenticator

#start
google-authenticator

#scan QR code from your phone app

#Configure /etc/pam.d/sshd file
sudo vi /etc/pam.d/sshd

#Comment out standard unix authentication

#Add “auth required pam_google_authenticator.so” at the last line.

#edit /etc/ssh/sshd_config  file
sudo vi /etc/ssh/sshd_config

#change ChallengeResponseAuthentication yes

#add this line after UsePAM
# AuthenticationMethods publickey,password publickey,keaboad-interactive

#restart sshd
sudo systemctl restart sshd

