#!/bin/bash
# Sublime build system script ~/.config/sublime-text-3/Packages/User/




rpath=$(dirname $(readlink -f $0))
cd $rpath

path=$rpath/dist
source $path/vars.sh

server=$rpath/src/server
backend=$rpath/src/backend
frontend=$rpath/src/frontend


mkdir -pv $nginx_chroot 2>&1 >/dev/null
mkdir -pv $tornado_chroot 2>&1 >/dev/null

#Clear
find . -type f -name "$backend/*.py[co]" -delete 2>&1 >/dev/null
find . -type d -name "$backend/__pycache__" -delete 2>&1 >/dev/null
/bin/rm $nginx_chroot/heap/*.css 2>&1 >/dev/null
/bin/rm -rf $tornado_chroot/heap 2>&1 >/dev/null
/bin/rm -rf $tornado_chroot/lib 2>&1 >/dev/null
/bin/rm -rf $tornado_chroot/template 2>&1 >/dev/null
/bin/rm -rf $tornado_chroot/*.py 2>&1 >/dev/null
/bin/rm -rf $tornado_chroot/parts/*.py 2>&1 >/dev/null
/bin/rm -rf $tornado_chroot/parts/glob.json 2>&1 >/dev/null
/bin/rm -rf $tornado_chroot/parts/greeting.json 2>&1 >/dev/null
/bin/rm -rf $tornado_chroot/parts/prof.json 2>&1 >/dev/null


#Copy
/bin/cp $server/heap/*.css $nginx_chroot/heap 2>&1 >/dev/null
/bin/cp -r $backend/lib $tornado_chroot 2>&1 >/dev/null
/bin/cp -r $backend/template $tornado_chroot 2>&1 >/dev/null
/bin/cp $backend/*.py $tornado_chroot 2>&1 >/dev/null
/bin/cp $backend/parts/*.py $tornado_chroot/parts 2>&1 >/dev/null
/bin/cp $backend/parts/glob.json $tornado_chroot/parts 2>&1 >/dev/null
/bin/cp $backend/parts/greeting.json $tornado_chroot/parts 2>&1 >/dev/null
/bin/cp $backend/parts/prof.json $tornado_chroot/parts 2>&1 >/dev/null
/bin/cp $rpath/src/version $tornado_chroot 2>&1 >/dev/null
/bin/chmod 775 -R $nginx_chroot 2>&1 >/dev/null

/bin/cp -r $nginx_chroot/heap $tornado_chroot 2>&1 >/dev/null