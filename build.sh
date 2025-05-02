#!/bin/bash
sudo docker build -t imgtimedb ./services/timedb
sudo docker build -t imgtimekeeper ./services/timekeeper
sudo docker build -t imgdb ./services/db
sudo docker build -t imgmanager ./services/manager
sudo docker build -t imgdistributor ./services/distributor
sudo docker build -t imghub ./services/hub
sudo docker build -t imgworker ./services/worker
