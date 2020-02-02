#!/bin/bash

# Change Project name
name=nk

nginx=$path/nginx
nginx_docker=${name}_nginx
nginx_run=${name}_nginx.server
nginx_chroot=$path/nginx_root
nginx_root=/usr/share/nginx/html
nginx_logs='docker logs '$nginx_run

tornado=$path/tornado
tornado_docker=${name}_tornado
tornado_run=${name}_tornado.server
tornado_chroot=$path/tornado_root
tornado_root=/usr/src/app

mongo=$path/mongo
mongo_docker=${name}_mongo
mongo_run=${name}_mongo.server
mongo_chroot=$path/mongo_db
mongo_root=/data/db
mongo_logs='docker logs '$mongo_run 

subnet=${name}_net
network_logs="docker network inspect ${subnet}|grep IPv4 -B 3"
