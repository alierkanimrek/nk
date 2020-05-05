#!/bin/bash
# Sublime build system script ~/.config/sublime-text-3/Packages/User/




rpath=$(dirname $(readlink -f $0))
cd $rpath

path=$rpath/dist
source $path/vars.sh

server=$rpath/src/server
backend=$rpath/src/backend
frontend=$rpath/src/frontend

mkdir -pv $nginx_chroot
mkdir -pv $tornado_chroot

#Clear
/bin/rm -rf $nginx_chroot/* 2>&1 >/dev/null
/bin/rm -rf $tornado_chroot/heap 2>&1 >/dev/null

#Copy
/bin/cp -Rv $server/* $nginx_chroot 2>&1 >/dev/null
/bin/cp -R $server/heap $tornado_chroot 2>&1 >/dev/null
/bin/cp -Rv $backend/* $tornado_chroot 2>&1 >/dev/null
/bin/cp  $rpath/src/version $tornado_chroot 2>&1 >/dev/null
/bin/chmod 775 -R $nginx_chroot 2>&1 >/dev/null