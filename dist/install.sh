#!/bin/bash

uname=alierkanimrek

path=$(dirname $(readlink -f $0))
cd $path
source $path/vars.sh
version="$(cat $path/../src/version)"
assetsurl=https://github.com/$uname/$name/releases/download/$version/assets_$version.tar.gz

echo -e "\nApp         : $name \nGithub User : $uname \nApp Version : $version"

if [ "$1" == "install" ];then
    /bin/cp -v appservice.service /lib/systemd/system/appservice.service
    systemctl daemon-reload
    target=/var/${name}
elif [ "$1" == "" ];then
    target=/var/${name}
else
    target=$1/${name}
fi
echo -e "\nTarget      : $target \nSource      : $path"

app=$target/app
nginx=$target/nginx
backup=$target/backup

#Prepare dirs
echo -e "\nPreparing dirs"
mkdir -pv $app
mkdir -pv $backup/app
mkdir -pv $nginx
mkdir -pv $backup/nginx

#Download assets
echo -e "\nDownloading Assets"
curl -L $assetsurl > assets_$version.tar.gz
OUT=$?
if ! [ $OUT -eq 0 ];then
    exit 1
fi

#Build
echo -e "\nBuilding App"
cd ..
bash ./build.sh
cd $path

#Place Assets
echo -e "\nExtracting Assets"
tar -xvf assets_$version.tar.gz -C $nginx_chroot/heap 2>&1 >/dev/null
OUT=$?
if ! [ $OUT -eq 0 ];then
    exit 1
fi

echo -e "\nReady to updating"

#Stop Services
echo -e "\nServices stopping"
systemctl stop nginx.service
systemctl stop appservice.service
sleep 5

#Backup App 
echo -e "\nBacking up current App"
/bin/rm -rf $backup/app/* 2>&1 >/dev/null
/bin/rm -rf $backup/nginx/* 2>&1 >/dev/null
/bin/cp -Rv $app/* $backup/app 2>&1 >/dev/null
/bin/cp -Rv $nginx/* $backup/nginx 2>&1 >/dev/null

#Cleaning App
echo -e "\nCleaning App"
/bin/rm -rf $app/* 2>&1 >/dev/null
/bin/rm -rf $nginx/* 2>&1 >/dev/null

#Update
echo -e "\nUpdating"
/bin/cp -Rv $tornado_chroot/* $app 2>&1 >/dev/null
/bin/cp -Rv $nginx_chroot/* $nginx 2>&1 >/dev/null

#Restoring conf, db and dynamic files
echo -e "\nRestoring conf etc."
/bin/cp -v $backup/app/config.conf $app 2>&1 >/dev/null
/bin/cp -v $backup/app/*.log* $app 2>&1 >/dev/null
/bin/cp -v $backup/nginx/heap/social/* $nginx/heap/social 2>&1 >/dev/null

#Edit for restoring dynamic files
/bin/cp -v $backup/app/parts/*.json $app/parts

#Chmod
echo -e "\nChmod Dirs"
chown -R admin:admin $app
chown -R admin:admin $nginx/heap/social
#chown -R nginx:nginx $nginx
chmod -R 775 $nginx
chmod -R 775 $app 

#Restart Services
echo -e "\nStarting Services"
systemctl start appservice.service
systemctl start nginx.service
