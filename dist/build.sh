#!/bin/bash
# Docker builder
: <<'COMMENT'
   
COMMENT


path=$(dirname $(readlink -f $0))
cd $path
source $path/vars.sh

cd $nginx
sudo docker build -t $nginx_docker .

#cd $mongo
#sudo docker build -t $mongo_docker .

#cd $tornado
#sudo docker build -t $tornado_docker .

cd ..
#sudo docker network create $subnet
echo .
docker network inspect $subnet|grep Subnet

echo You should check and fix ip adresses of tornado and mongo servers 
echo at nginx.conf and server.py file according to your docker sub-network
echo First, run your dockers and get ip adresses from network watch window
echo then fix them, rebuild nginx and restart all