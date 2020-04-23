#!/bin/bash

path=$(dirname $(readlink -f $0))
cd $path
source $path/vars.sh

if [ "$1" == "install" ];then
    /bin/cp -v appservice.service /lib/systemd/system/appservice.service
    systemctl daemon-reloadelse
    path=/var/${name}
elif [ "$1" == "" ];then
    path=/var/${name}
else
    path=$1/${name}
fi

app=$path/app
nginx=$path/nginx
backup=$path/backup

systemctl stop nginx.service
systemctl stop appservice.service

mkdir -p $app
mkdir -p $backup/app

/bin/rm -rf $backup/*
/bin/cp -Rv $app/* $backup/app
/bin/rm -rf $app/*
/bin/cp -Rv tornado_root/* $app
/bin/cp -v $backup/app/config.conf $app
/bin/cp -v $backup/app/*log* $app
/bin/cp -v $backup/app/parts/*.json $app/parts

mkdir -p $nginx
mkdir -p $backup/nginx

/bin/cp -Rv $nginx/* $backup/nginx
/bin/rm -rf $nginx/*
/bin/cp -Rv nginx_root/* $nginx
/bin/cp -v $backup/nginx/heap/social/* $nginx/heap/social

chown -R admin:admin $app
chown -R admin:admin $nginx/heap/social
#chown -R nginx:nginx $nginx
chmod -R 775 $nginx
chmod -R 775 $app 

systemctl start appservice.service
systemctl start nginx.service