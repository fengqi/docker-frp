#!/bin/sh

if [ ! -d "/data" ];then
    mkdir /data;
fi

if [ ! -f "/data/frps.ini" ];then
    cp /etc/frps.ini /data/frps.ini;
fi

/usr/local/bin/frps -c /data/frps.ini
