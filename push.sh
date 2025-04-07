#!/bin/bash
ADDR=192.168.1.93:9000
VER=12

sudo docker tag imgmanager $ADDR/imgmanager:v$VER
sudo docker tag imgdistributor $ADDR/imgdistributor:v$VER
sudo docker tag imghub $ADDR/imghub:v$VER
sudo docker tag imgworker $ADDR/imgworker:v$VER
sudo docker tag imgdb $ADDR/imgdb:v$VER

sudo docker push $ADDR/imgmanager:v$VER
sudo docker push $ADDR/imgdistributor:v$VER
sudo docker push $ADDR/imghub:v$VER
sudo docker push $ADDR/imgworker:v$VER
sudo docker push $ADDR/imgdb:v$VER

