#!/bin/bash
# Sublime build system script ~/.config/sublime-text-3/Packages/User/

# This source file is part of the rpdev open source project
#    Copyright 2018 Ali Erkan IMREK and project authors
#    Licensed under the MIT License 








path=$(dirname $(readlink -f $0))
cd $path
source $path/vars.sh
heap=$nginx_chroot/heap

version="$(cat $tornado_chroot/version)"
rm assets*.tar.gz
tar -zcvf assets_$version.tar.gz -C $heap glob greeting icons prof

