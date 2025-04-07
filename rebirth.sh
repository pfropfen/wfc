#!bin/bash
sudo docker container stop $(sudo docker ps -a) && sudo docker container rm $(sudo docker ps -a)
kubectl delete -f wfcdeploy.yaml
kubectl delete --all pods --grace-period=0 --force
sudo docker image rm -f $(sudo docker image ls)
bash build.sh
bash push.sh
kubectl apply -f wfcdeploy.yaml
