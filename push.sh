#!/bin/bash
ADDR=pfropfen
VER=latest

sudo docker tag imgmanager $ADDR/imgmanager:$VER
sudo docker tag imgdistributor $ADDR/imgdistributor:$VER
sudo docker tag imghub $ADDR/imghub:$VER
sudo docker tag imgworker $ADDR/imgworker:$VER
sudo docker tag imgdb $ADDR/imgdb:$VER
sudo docker tag imgtimedb $ADDR/imgtimedb:$VER
sudo docker tag imgtimekeeper $ADDR/imgtimekeeper:$VER

sudo docker push $ADDR/imgmanager:$VER
sudo docker push $ADDR/imgdistributor:$VER
sudo docker push $ADDR/imghub:$VER
sudo docker push $ADDR/imgworker:$VER
sudo docker push $ADDR/imgdb:$VER
sudo docker push $ADDR/imgtimedb:$VER
sudo docker push $ADDR/imgtimekeeper:$VER


