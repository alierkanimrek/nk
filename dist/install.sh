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
mkdir -p $backup

/bin/rm -rf $backup/*
/bin/cp -v $app/*.conf $backup
/bin/cp -v $app/*.log.* $backup
/bin/cp -v $app/*.log $backup
/bin/rm -rf $app/*
/bin/cp -Rv tornado_root/* $app
/bin/cp -v $backup/* $app

mkdir -p $nginx
/bin/rm -rf $nginx/*
/bin/cp -Rv nginx_root/* $nginx

chmod -R 775 $nginx
chmod -R 775 $app 

systemctl start appservice.service
systemctl start nginx.service