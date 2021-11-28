#!/bin/sh
#How to install a WAF (shadow daemon) for Amazon Linux

#ssh into the server

#update
sudo yum update -y

#install docker
sudo amazon-linux-extras install docker -y

#Install a docker-compose from github
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#Give an execute permission
sudo chmod +x /usr/local/bin/docker-compose

#Create a synbolic link
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

#Start and enable docker service
sudo systemctl enable docker & systemctl start docker

#Install git
sudo yum install git -y

#Clone repo
git clone https://github.com/zecure/packaging & cd packaging/docker/compose

#Install and start Shadow Daemon
sudo ./shadowdctl up -d

#Create an admin user for the console
sudo ./shadowdctl exec web ./app/console swd:register --admin --name=admin
