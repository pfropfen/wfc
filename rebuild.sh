#!/bin/bash
ADDR=pfropfen
VER=latest
SERVICE=$1
IMAGE="img$1"

sudo docker image rm $IMAGE
sudo docker build -t $IMAGE ./services/$SERVICE
sudo docker tag $IMAGE $ADDR/$IMAGE:$VER
sudo docker push $ADDR/$IMAGE:$VER
