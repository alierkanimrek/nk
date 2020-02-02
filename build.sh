#!/bin/bash
# Sublime build system script ~/.config/sublime-text-3/Packages/User/




path=$(dirname $(readlink -f $0))
cd $path
server=$path/src/server
backend=$path/src/backend
frontend=$path/src/frontend
nginx=$path/dist/nginx_root
tornado=$path/dist/tornado_root

#Clear
/bin/rm -rf $nginx/* > /dev/null 2>&1
/bin/rm -rf $tornado/heap > /dev/null 2>&1

#Copy
/bin/cp -Rv $server/* $nginx 
/bin/cp -Rv $server/heap $tornado 
/bin/cp -Rv $backend/* $tornado 
/bin/chmod 775 -R $nginx