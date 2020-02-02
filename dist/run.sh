#!/bin/bash
#Run Dockers
: <<'COMMENT'
   
COMMENT





path=$(dirname $(readlink -f $0))
cd $path
source $path/vars.sh


help() {
    echo 'Usage: run.sh start|stop server|app init'
}


stop (){
    docker stop $nginx_run &>/dev/null
    docker rm $nginx_run &>/dev/null
    #docker stop $mongo_run &>/dev/null
    #docker rm $mongo_run &>/dev/null
}


watch(){
    gnome-terminal --tab -- watch -c $nginx_logs
    #gnome-terminal --tab -- watch -c $mongo_logs
    gnome-terminal --tab -- watch -c $network_logs
}


nginx () {
    docker run --name $nginx_run -d --network $subnet -p 443:443 -v $nginx_chroot:$nginx_root $nginx_docker
}

mongo () {
    echo
    #docker run --name $mongo_run -d --network $subnet -p 27017:27017 -v $mongo_chroot:$mongo_root $mongo_docker
}


#--add-host outside:172.17.0.1
tornado (){
    echo
    gnome-terminal -- docker run -it --name $tornado_run --network $subnet -p 8000:8000 -v $tornado_chroot:/usr/src/app -w /usr/src/app $tornado_docker bash ./run.sh
    echo "docker exec -it " $tornado_run " /bin/bash"
}


mongo_init(){
    echo "Run command"
    #echo 'docker exec -ti '$mongo_run' sh -c "cd /;mongo < init.js"'
}



if [ "$1" == "start" ];then

    if [ "$2" == "server" ];then
        echo -e "Run servers"
        stop
        nginx
        mongo
        watch
        if [ "$3" == "init" ];then
            mongo_init
        fi
    elif [ "$2" == "app" ];then
        echo -e "Run app"
        docker stop $tornado_run &>/dev/null
        docker rm $tornado_run &>/dev/null
        tornado
    else
        ./run.sh start server
    ./run.sh start app
    fi

elif [ "$1" == "stop" ];then

    if [ "$2" == "server" ];then
        echo -e "Stop servers"
        stop   
    elif [ "$2" == "app" ];then
        echo -e "Stop app"
        docker stop --time 1 $tornado_run &>/dev/null
        docker rm $tornado_run &>/dev/null
    else
        ./run.sh stop app
    ./run.sh stop server
    fi

else
    help    
fi
