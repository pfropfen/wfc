sudo docker ps -a
sudo apt-get update
python3
sudo apt update
ifconfig
sudo apt install net-tools
sudo nano ~/.bashrc
restart
reboot
ifconfig
shutdown now
hostname
ifconfig
sudo hostname set-hostname vm1
hostname
sudo hostname set-hostname vm1
reboot
sudo bin/bash
sudo /bin/bash
hostname
shutdown now
hostname
ifconfig
shutdown now
ifconfig
sudo swapoff -a
sudo sed -i '/swap/s/^/#/' /etc/fstab
sudo swapon --show
sudo nano /etc/hosts
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf overlay br_netfilter EOF
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward = 1
EOF

sudo sysctl --system
sudo apt update
sudo apt install curl ca-certificates apt-transport-https
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/core:/stable:/v1.26.5/deb/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
curl -fsSL https://pkgs.k8s.io/core:/stable:/v.1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
curl -fsSL https://pkgs.k8s.io/core:/stable:/v.1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
curl -fsSL https://pkgs.k8s.io/core:/stable:/v.1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v.1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo apt-get update
curl -fsSL https://pkgs.k8s.io/core:/stable:/v.1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt install kubelet kubeadm kubectl
sudo mkdir /etc/containerd
sudo sh -c "containerd config default > /etc/containerd/config.toml"
sudo apt install docker.io
sudo mkdir /etc/containerd
sudo sh -c "containerd config default > /etc/containerd/config.toml"
sudo sed -i 's/ SystemCgroup = false/ SystemCgroup = true/' /etc/containerd/config.toml
sudo systemctl restart conainerd.service
sudo containerd start
sudo systemctl restart conainerd.service
sudo containerd start -d
sudo systemctl enable containerd.service
sudo systemctl restart conainerd.service
sudo systemctl restart kubelet.service
sudo systemctl enable kubelet.service
sudo systemctl daemon-reload
sudo systemctl enable --now containerd
sudo systemctl restart containerd.service
sudo systemctl restart kubelet.service
sudo systemctl enable kubelet.service
sudo sh -c "containerd config default > /etc/containerd/config.toml"
sudo sed -i 's/ SystemdCgroup = false/ SystemdCgroup = true/' /etc/containerd/config.toml
sudo systemctl restart containerd.service
sudo systemctl restart kubelet.service
sudo systemctl enable kubelet.service
cd /etc/containerd/
sudo nano config.toml
cls
clear
sudo kubeadm config images pull
sudo kubeadm init --pod-network-cidr=10.10.0.0/16
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/tigera-operator.yaml
curl https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/custom-resources.yaml -O
sudo curl https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/custom-resources.yaml -O
ls -l
sudo rm custom-resources.yaml
ls -a
cd ..
lsw -a
ls
cd home
ls
cd pfropfen
sudo curl https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/custom-resources.yaml -O
ls -l
sed -i 's/cidr: 192\.168\.0\.0\/16/cidr: 10.10.0.0\/16/g' custom-resources.yaml
kubectl create -f custom-resources.yaml
clear
kubectl get nodes
kubectl get pods -A
shutdown now
psa
kubectl show nodes
kubectl nodes
kubectl get nodes
ifconfig
sudo nano /etc/network/interfaces
cd etc
cd /etc
cd network
ls -a
cd ..
sudo nano /etc/network/interfaces
sudo nano /etc/netplan
cd /etc/netplan
ls -a
sudo nano 50-cloud-init.yaml 
sudo bash -c 'echo "network: {config: disabled}" > /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg'
sudo netplan apply
sudo nano 50-cloud-init.yaml 
sudo netplan apply
ifconfig
shutdown now
kubectl get services
kubectl get nodes
what the fuck
sudo kubeadm reset
kubectl get services
reboot
ps
ps -a
sudo kubeadm reset
kubectl get services
kubectl get nodes
ps
ps -A
sudo kubeadm config images pull
ping google.de
ifconfig
ping www.google.com
cd /etc/netplan
ls -a
sudo nano 50-cloud-init.yaml 
sudo netplan try
sudo nano 50-cloud-init.yaml 
sudo netplan try
ifconfig
ping google.de
ping4 google.de
sudo netplan apply
sudo kubeadm config images pull
cd ../..
ls -a
cd /home/pfropfen
kubeadm init --pod-network-cidr=10.10.0.0/16
sudo kubeadm init --pod-network-cidr=10.10.0.0/16 > token.sh
sudo nano token.sh
sudo touch onlytoken.sh
sudo nano onlytoken.sh 
sudo rm onlytoken.sh 
sudo nano token.sh
python3 -m http.server
sudo nano token.sh
nano tok
sudo nano token.sh
nano tok
sudo nano token.sh
ls -a
sudo rm .kube
sudo rmdir .kube
sudo rmdir .kube -f
sudo rmdir .kube -F
cd .kube
ls -a
sudo rm config
cd ..
sudo cp -i /etc/kuberbetes/admin.conf $HOME/.kube/config
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl get nodes
kubectl get services
kubectl get pods
kubectl get pods -a
kubectl get pods -A
kubectl logs
kubectl logs coredns-7db6d8ff4d-kcg8k
kubectl get pods -A
kubectl logs etcd-vm1
kubectl get pods
kubectl get pods -A
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/tigera-operator.yaml
kubectl get pods
kubectl get pods -A
curl https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/custom-resources.yaml -O
ls -l
sed -i 's/cidr: 192\.168\.0\.0\/16/cidr: 10.10.0.0\/16/g' custom-resources.yaml
kubectl create -f custom-resources.yaml
kubectl get pods -A
curl 192.168.1.190:8000/services.zip > services.zip
curl 192.168.1.190:8000/services.zip
curl 192.168.1.190:8000/services.zip -O
ls -a
unzip
sudo apt install unzip
unzip services.zip
ls -a
mkdir services
mv hub.py /services
sudo mv hub.py services/hub.py
ls -a
cd services
ls -a
cd ..
ls -a
sudo rm hubtest.py
sudo mv TILES services/TILES
ls -a
sudo mv kafkaconsumer.py services/kafkaconsumer.py
sudo mv manager.py services/manager.py
sudo mv restrictions.xlsx services/restrictions.xlsx
sudo mv visualization.py services/visualization.py
sudo rm kafkatest.py
sudo mv maploader services/maploader.py
sudo mv maploader.py services/maploader.py
sudo mv rules.xlsx services/rules.xlsx
sudo mv wavefunctionlookup.py services/wavefunctionlookup.py
sudo mv templates services/templates
sudo mv wave.py services/wave.py
sudo mv distributor.py services/distributor.py
sudo mv worker.py services/worker.py
ls -a
cd servicesw
cd services
clear
ls -a
mkdir manager
sudo mv manager.py manager/manager.py
sudo mv rules.xlsx manager/rules.xlsx
sudo mv restrictions.xlsx manager/restrictions.xlsx
ls -a
mkdir distributor
sudo mv distributor.py distributor/distributor.py
sudo mv templates distributor/templates
sudo cp wave.py distributor/wave.py
mkdir hub
sudo mv hub.py hub/hub.py
sudo rm kafkaconsumer.py
ls -a
sudo rm maploader.py 
sudo rm visualization.py 
sudo cp wavefunctionlookup.py distributor/wavefunctionlookup.py
mkdir worker
sudo cp wave.py worker/wave.py
sudo cp wavefunctionlookup.py worker/wavefunctionlookup.py
sudo mv worker.py worker/worker.py
ls -a
sudo rm wave.py
sudo rm wavefunctionlookup.py 
ls -a
sudo rm -f TILES
sudo rmdir -f TILES
sudo rmdir TILES
sudo rmdir TILES -F
sudo rm -r -f TILES
ls -a
cd manager
ls -a
sudo nano dockerfile
sudo rm dockerfile
ls -a
sudo nano Dockerfile
ls -a
sudo docker build -t managerimg .
sudo docker run managerimg
ls -a
sudo docker image rm managerimg
sudo docker image rm managerimg -f
sudo nano Dockerfile
ls -a
docker build -t wfcmanager .
sudo docker build -t wfcmanager .
docker image ls
sudo docker image ls
sudo docker run wfcmanager
psa
killall
psa
sudo docker run wfcmanager
psa
logs brave_germain
logs 243e650d917c
logs brave_germain
sudo docker logs brave_germain
sudo docker exec -it brave_germain /bin/bash
sudo nano Dockerfile
killall
sudo docker image ls
sudo docker image rm wfcmanager
sudo docker build -t wfcmanager .
sudo docker image rm wfcmanager
sudo nano Dockerfile 
sudo docker build -t wfcmanager .
sudo docker run wfcmanager
psa
logs zen_kapitsa
sudo nano Dockerfile
killall
sudo docker image rm wfcmanager
sudo docker build -t wfcmanager .
psa
sudo docker run wfcmanager
psa
killall
sudo docker image rm wfcmanager
sudo nano Dockerfile 
sudo docker build -t wfcmanager .
sudo docker run wfcmanager
psa
killall
sudo docker image rm wfcmanager
sudo nano Dockerfile 
sudo docker build -t wfcmanager .
sudo docker run wfcmanager
killall
sudo docker image rm wfcmanager
sudo nano Dockerfile 
psa
sudo docker image ls
sudo docker build -t wfcmanager .
sudo docker run wfcmanager
killall
sudo docker image rm wfcmanager
sudo nano Dockerfile 
sudo docker build -t wfcmanager .
sudo docker run wfcmanager
psa
sudo docker start interesting_chatelet -d
sudo docker start -d interesting_chatelet
sudo docker start -i interesting_chatelet
sudo docker run -i interesting_chatelet
psa
sudo docker run -d interesting_chatelet
sudo docker container start -d interesting_chatelet
sudo docker container start -i interesting_chatelet
killall
sudo docker container run -d wfcmanager
psa
logs compassionate_clarke
ifconfig
psa
k
sudo docker image rm wfcmanager
sudo nano Dockerfile 
sudo docker build -t wfcmanager .
sudo docker run wfcmanager -p 5000:5000 -d
sudo docker run -p 5000:5000 -d --name manage wfcmanager
psa
logs manage
killall
sudo docker image rm wfcmanager
sudo nano Dockerfile 
sudo nano manager.py
clear
sudo docker build -t wfcmanager .
sudo docker run -p 5000:5000 -d --name manage wfcmanager
psa
logs manage
killall
sudo docker image rm wfcmanager
sudo nano Dockerfile 
sudo docker build -t wfcmanager .
sudo docker run -p 5000:5000 -d --name manage wfcmanager
psa
killall
shutdown now
ifconfig
kubectl get nodes
kubectl get pods
kubectl get pods -A
kubectl cluster-info
kubectl get pods -A
ls -a
cd services
cd manager
dir
ls -a
psa
cd ..
sudo cp ./manager/Dockerfile ./distributor/Dockerfile
cd distributor
ls -a
sudo nano Dockerfile 
sudo docker build -t wfcdistributor .
sudo docker run -p 5001:5001 -d --name distributor wfcdistributor
psa

ls -a
sudo nano Dockerfile
clear
cd ..
mkdir db
cd db
curl 192.168.1.190:8000/docker-compose.yaml -O
curl 192.168.1.190:8000/init.sql -O
ls
psa
killall
psa
sudo docker-compose up -d
psa
üsa
psa
killall
shutdown now
psa
cd services
ls 
cd distributor/
ls
sudo nano Dockerfile
sudo kubectl get nodes
kubectl get nodes
kubectl get pods
kubectl get pods -A
cd ..
cd hub
ls
cd ..
cd manager
ls
sudo nano Dockerfile
cd ..
cd .
cd ..
rm -rf services
ls
rm services.zip
ls
cd db
ls
sudo nano docker-compose.yaml
clear
killimg
killall
sudo docker image ls
clear
sudo curl 192.168.1.190:8000/services.zip -O
sudo unzip services.zip
ls
sudo rm -rf services
sudo rm services.zip
ls
cd ..
sudo rm -rf db
ls
sudo curl 192.168.1.190:8000/services.zip -O
sudo unzip services.zip
ls
sudo rm services.zip
ls
cd services
ls
sudo sh buildimages.sh
sudo bash buildimages.sh
sudo nano buildimages.sh 
sudo sh buildimages.sh
sudo bash buildimages.sh
sudo nano buildimages.sh 
sudo bash buildimages.sh
ls
sudo nano buildimages.sh 
sudo bash buildimages.sh
sudo nano buildimages.sh 
sudo bash buildimages.sh
sudo nano buildimages.sh 
sudo bash buildimages.sh
sudo nano buildimages.sh 
sudo bash buildimages.sh
sudo nano build.sh
sudo bash build.sh
killall
killimg
sudo docker image ls
ls
sudo rm build.sh
sudo rm buildimages.sh
cd ..
sudo nano build.sh
ls
sudo bash build.sh
sudo docker image ls
kubectl get nodes
kubectl get pods
kubectl get pods -A
cd services
ls
kubectl apply -f wfcdeploy.yaml
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml
sudo rm wfcdeploy.yaml 
sudo curl 192.168.1.190:8000/wfcdeploy.yaml -O
ls
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml
kubectl get pods
kubectl get pods -A
sudo docker image ls
sudo docker run -d -p 9000:9000 --restart always --name registry registry
cd ..
ls
sudo nano push.sh
sudo nano wfcdeploy.yaml 
cd services
sudo nano wfcdeploy.yaml 
ls
cd ..
ls
cd services
sudo nano wfcdeploy.yaml 
psa
kubectl apply -f wfcdeploy.yaml
kubectl get pods
kubectl rollout history
kubectl rollout history deployment/app
kubectl get deployment
kubectl rollout undo
kubectl rollout undo deployment
kubectl get deployment
kubectl get pods
kubectl rollout undo deployment
kubectl get pods
kubectl delete -f wfcdeploy.yaml
kubectl get pods
kubectl get nodes
kubectl get pods
kubectl apply -f wfcdeploy.yaml
kubectl get pods
sudo nano wfcdeploy.yaml 
sudo docker image ls
sudo docker registry ls
curl -X GET https://192.168.1.93:9000/v2/_catalog
psa
logs registry
kubectl delete -f wfcdeploy.yaml
killall

sudo docker run -d -p 9000:5000 --restart always --name registry registry
cd ..
ls
sudo bash push.sh
psa
curl -X GET https://192.168.1.93:9000/v2/_catalog
curl -X GET https://192.168.1.93:9000/v3/_catalog
curl -X GET https://192.168.1.93:9000/v1/_catalog
curl -X GET https://192.168.1.93:9000/v4/_catalog
curl -X GET https://192.168.1.93:5000/v2/_catalog
curl -X GET https://192.168.1.93:9000/
curl -X GET https://192.168.1.93:9000
curl -X GET http://192.168.1.93:9000/v2/_catalog
sudo nano push.sh
sudo nano wfcdeploy.yaml 
cd services
sudo nano wfcdeploy.yaml 
kubectl delete -f wfcdeploy.yaml
cd ..
kubectl delete -f wfcdeploy.yaml
sudo docker image ls
sudo bash push.sh
sudo docker image ls
psa
curl -X GET http://192.168.1.93:9000/v2/_catalog
curl -X GET https://192.168.1.93:9000/v2/_catalog
sudo docker image ls
kubectl apply -f wfcdeploy.yaml
cd services
kubectl apply -f wfcdeploy.yaml
psa
kubectl get pods
sudo nano wfcdeploy.yaml
cd ..
sudo nano push.sh
psa
killall
killimg
ls
sudo bash build.sh
kubectl get pods
kubectl delete -f wfcdeploy.yaml
cd services
kubectl delete -f wfcdeploy.yaml
kubectl get pods
psa
sudo docker image ls
kubectl get pods
kubectl get nodes
kubectl get pods
reboot now
reboot
sudo reboot now
kubectl get pods
kubectl get nodes
ifconfig
kubectl get nodes
kubectl get pods
sudo docker image ls
sudo docker run -d -p 9000:5000 --restart always --name registry registry:2
ls
bash build.sh
psa
bash push.sh
sudo docker image ls
cd services
ls
curl -X 192.168.1.93:9000/v2/_cataglog
curl -X https://192.168.1.93:9000/v2/_catalog
curl -X GET https://192.168.1.93:9000/v2/_catalog
curl -X GET http://192.168.1.93:9000/v2/_catalog
curl -X GET https://192.168.1.93:9000/v2/_catalog
psa
cd ..
sudo nano push.sh
cd services
ls
sudo docker image ls
sudo docker image rm 192.168.1.93:9000/imgworker
sudo docker image rm 192.168.1.93:9000/imgworker:v12
sudo docker image rm imgworker
sudo docker image ls
sudo docker pull 192.168.1.93:9000/imgworker:v12
sudo docker pull http://192.168.1.93:9000/imgworker:v12
sudo docker pull https://192.168.1.93:9000/imgworker:v12
c d..
sudo nanp /etc/docker/daemon.json
sudo nano /etc/docker/daemon.json
cd ..
killimg
sudo docker image ls
killimg
killall
killimg
sudo docker image ls
psa
bash build.sh
psa
sudo docker run -d -p 9000:5000 --restart always --name registry registry:2
sudo docker image ls
ls
bash push.sh
sudo systemctl restart docker
psa
killall
sudo systemctl restart docker
systemctl restart docker
sudo systemctl restart docker
sudo service docker restart
psa
sudo service docker start
psa
shutdown now
psa
sudo docker image ls
sudo docker run -d -p 9000:5000 --restart always --name registry registry:2
ls
bash push.sh
curl -X GET http:/192.168.1.93:9000/v2/_catalog
curl -X GET https:/192.168.1.93:9000/v2/_catalog
sudo nano /etc/docker/daemon.json
killall
sudo nano /etc/docker/daemon.json
sudo service docker restart
psa
sudo docker run -d -p 9000:5000 -restart always --name registry registry:2
sudo docker run -d -p 9000:5000 --restart always --name registry registry:2
ls
bash push.sh
sudo docker image ls
bash build.sh
psa
bash push.sh
sudo docker image ls
killall
shutdown now
psa
b
ls
sudo docker image ls
kubectl get nodes
kubectl get pds
kubectl get pods
kubectl get pods -A
clear
kubectl get pods -A
sudo docker run -d -p 9000:5000 --restart always --name registry registry:2
bash push.sh
sudo nano /etc/docker/daemon.json
ifconfig
sudo service docker retart
sudo service docker restart
bash push.sh
psa
bash push.sh
sudo bash push.sh
sudo nano /etc/docker/daemon.json
killall
killimg
psa
sudo docker image ls
bash build.sh
sudo docker run -d -p 9000:5000 --restart always --name registry registry:2
bash push.sh
psa
sudo docker image ls
psa
sudo nano /etc/docker/daemon.json
sudo service docker restart
bash push.sh
sudo nano push.sh
sudo nano /etc/docker/daemon.json
sudo service docker restart
bash push.sh
sudo nano /etc/docker/daemon.json
sudo service docker restart
bash push.sh
psa
sudo nano /etc/docker/daemon.json
bash push.sh
sudo nano /etc/docker/daemon.json
sudo systemctl restart docker
bash push.sh
sudo nano /etc/docker/daemon.json
killall
sudo service docker restart
sudo systemctl restart docker
psa
bash push.sh
sudo docker run -d -p 9000:5000 --restart always --name registry registry:2
psa
bash push.sh
brc
psa
bash push.sh
sudo nano /etc/docker/daemon.json
sudo systemctl daemon-reload
bash push.sh
psa
killall
shutdown now
psa
startreg
bash push.sh
psa
sudo docker image -ls
sudo docker image ls
sudo nano push.sh
sudo nano /etc/docker/daemon.json
sudo service docker restart
psa
sudo nano push.sh
bash push.sh
killall
startreg
bash push.sh
sudo nano /etc/docker/daemon.json
sudo service docker restart
killall
sudo service docker restart
startreg
bash push.sh
sudo docker info
sudo docker info | grep -A 20 "Insecure Registries"
cat ~/.docker/daemon.json
sudo cp /etc/docker/daemon.json ~/.docker/daemon.json
psa
cat /etc/buildkit/buildkitd.toml
sudo cat /etc/buildkit/buildkitd.toml
sudo cat ~/.config/buildkit/buildkitd.toml
psa
sudo bash push.sh
sudo nano /etc/containers/registries.conf
cd /etc/containers
cd /etc/
sudo nano /etc/docker/daemon.json
psa
killall
sudo service docker restart
mkdir containers
cd ..
sudo nano /etc/systemd/system/multi-user.target.wants/docker.service
sudo systemctl daemon-reload
sudo systemctl restart docker
psa
startreg
bash push.sh
ls
cd pfropfen
cd ~/
bash push.sh
sudo nano /etc/systemd/system/multi-user.target.wants/docker.service
cd etc
cd /etc
cd containers
sudo mkdir containers
cd ..
sudo nano /etc/default/docker
sudo systemctl reload docker
sudo systemctl daemon.reload
sudo systemctl daemon-reload
psa
killall
startreg
bash push.sh
cd ~/
bash push.sh
psa
sudo systemctl stop docker
sudo systemctl start docker
psa
bash push.sh
killall
sudo systemctl stop docker
sudo systemctl start docker
startreg
bash push.sh
sudo docker info
sudo nano /etc/docker/daemon.json
sudo systemctl daemon-reload
sudo systemctl stop docker
sudo systemctl start docker
psa
bash push.sh
shutdown now
psa
bash push.sh
sudo docker imaqge ls
sudo docker imaage ls
sudo docker image ls
sudo docker info
sudo nano /etc/docker/daemon.json
sudo nano /etc/systemd/system/multi-user.target.wants/docker.service
sudo nano /etc/docker/daemon.json
sudo docker info
ls /var/lib/docker
sudo ls /var/lib/docker
ls ~/.config/docker/
sudo ls ~/.config/docker/
sudo systemctl daemon-reload
sudo ls /etc/docker/
sudo nano /etc/docker/daemon.json
sudo service docker restart
psa
bash push.sh
sudo docker info
sudo ls /etc/systemd/system/docker.service.d
sudo ls /etc/systemd/system/
sudo ls /etc/systemd/system/docker.service.d
sudo nano /etc/systemd/system/docker.service
sudo systemctl enable docker
sudo systemctl edit docker.service
sudo nano /var/snap/docker/current/config/daemon.json
sudo service docker restart
psa
sudo docker info
sudo systemctl daemon-reload
sudo systemctl restart docker
sudo docker info
bash push.sh
which docker
sudo docker config inspect
sudo docker config
sudo nano push.sh
psa
bash push.sh
sudo nano push.sh
bash push.sh
sudo nano push.sh
bash push.sh
sudo nano push.sh
sudo systemctl status docker.service
sudo nano /etc/default/docker
sudo service docker restart
psa
sudo docker info
sudo nano /lib/systemd/system/docker.service
sudo systemctl daemon-reload
sudo service docker restart
sudo docker info
psa
killall
shutdown now
sudo docker info
psa
startreg
bash push.sh
sudo nano /lib/systemd/system/docker.service
sudo nano /etc/default/docker
sudo nano /var/snap/docker/current/config/daemon.json
sudo snap stop docker
sudo snap start docker
psa
sudo docker info
bash push.sh
psa
sudo docker image ls
ls
kubectl get nodes
kubectl get pods
kubectl get pods -A
cd services
ls
kubectl apply -f wfcdeploy.yaml
kubectl get pods
sudo nano wfcdeploy.yaml
kubectl get pods
kubectl describe pod wfcdb-depl
kubectl get pods
sudo ls /etc/rancher
kubectl delete -f wfcdeploy.yaml
sudo nano /etc/containerd/config.toml
sudo nano /etc/containers/registries.conf
sudo containerd --version
sudo nano /etc/containerd/config.toml
sudo containerd --version
sudo nano /etc/containerd/config.toml
sudo systemctl restart containerd
psa
sudo systemctl restart containerd
shutdown now
psa
cd services
kubectl apply -f wfcdeploy.yaml
sudo nano /etc/containerd/config.toml
kubectl apply -f wfcdeploy.yaml
kubectl apply -f wfcdeploy.yaml --validate=false

sudo nano /etc/containerd/config.toml
psa
sudo systemctl restart containerd
shutdown now
psa
kubectl get nodes
kubectl get pods
psa
sudo nano /etc/containerd/config.toml
sudo systemctl restart containerd
kubectl get pods
sudo service kubectl restart
shutdown now
kubectl get nodes
shutdown now
kubectl status
kubectl get nodes
sudo nano /etc/containerd/config.toml
kubectl --status
kubectl --help
kubectl cluster-info
kubectl get nodes
kubectl get pods -A
psa
kubectl get pods
ls
curl 192.168.1.190:8000/ssl.sh -O
ls
cat ssl.sh
sudo bash ssl.sh
cat ssl.sh | tee sslscript.sh
cat sslscript.sh 
bash sslscript.sh 
sudo apt install openssl
sudo nano sslscript.sh 
cat ssl.sh > ssls.sh
cat ssls.sh
bash ssls.sh
sudo rm ssl.sh
sudo rm ssls.sh
sudo rm sslscript.sh
curl 192.168.1.190:8000/ssl.sh -O
ls
replace --help
cp ssl.sh ssll.sh
rm ssl.sh
sed 's/\r$//' ssll.sh > ssl.sh
cat ssl.sh
bash ssl.sh
sudp bash ssl.sh
sudo bash ssl.sh
sudo nano ssl.sh
htpasswd
sudo apt install apache2-utils
sudo apt install openssl
sudo nano ssl.sh
sudo bash ssl.sh
sudo nano ssl.sh
sudo bash ssl.sh
ls /root/auth
sudo ls /root/auth
sudo mkdir /root/auth
sudo bash ssl.sh
sudo nano ssl.sh
sudo bash ssl.sh
sudo nano ssl.sh
su
su!
su
sudo /bin/bash
psa
killall
sudo /bin/bash
psa
sudo /bin/bash
psa
sudo /bin/bash
ls
cd ~"/
exit

exit
ls
sudo rm ssll.sh
sudo rm ssl.sh
sudo /bin/bash
ls
sudo ssl.sh
sudo nano ssl.sh
sudo bash ssl.sh
psa
sudo nano ssl.sh
sudo bash ssl.sh
psa
sudo nano ssl.sh
sudo bash ssl.sh
sudo nano ssl.sh
sudo bash ssl.sh
sudo nano ssl.sh
sudo ls /certs/
sudo nano ssl.sh
/certs
cd /certs
ls
cd ..
ls
cd ~
ls
sudo bash ssl.sh
sudo nano ssl.sh
sudo bash ssl.sh
sudo nano ssl.sh
sudo bash ssl.sh
sudo nano ssl.sh
sudo bash ssl.sh
sudo nano ssl.sh
cd /root
sudo cd /root
sudo cd /root/user
sudo ls /root
cd /certs
ls
cd ~/
sudo ls /root/certs/
sudo cp /certs/server.crt /root/certs/server.crt
sudo cp /certs/server.csr /root/certs/server.csr
sudo cp /certs/server.key /root/certs/server.key
sudo ls /root/certs/
ls
sudo nano ssl.sh#
sudo nano ssl.sh
sudo bash ssl.sh
sudo nano ssl.sh
psa
sudo bash ssl.sh
psa
curl https://192.168.1.93:9000/v2/_catalog
curl -Isk https://192.168.1.93:9000/v2
curl -ks -u root:nature https://192.168.1.93:9000/v2/_catalog
curl -ks -u root:password https://192.168.1.93:9000/v2/_catalog
ls
sudo bash push.sh
sudo nano push.sh
sudo docker login -u root 
sudo docker login https://192.168.1.93:9000 -u root
sudo bash push.sh
sudo docker image ls
cat ~/.docker/config.json
cat /var/snap/.docker/config.json
cat /var/snap/docker/config.json
ls /var/snap/docker/
ls /var/snap/docker/current
ls /var/snap/docker/current/config
ls -a /var/snap/docker/current/config
ls -a /var/snap/docker/current
kubectl create secret docker-registry dockerauth
kubectl create secret docker-registry dockerauth --docker-username=root --docker-password=password
ls
cd services
sudo nano wfcdeploy.yaml 
psa
kubectl apply -f wfcdeploy.yaml 
kubectl get pods
kubectl logs wfcdb-dep
kubectl logs wfcdb-deployment-59
kubectl logs wfcdb-deployment-59c5948c94-bqkmp
kubectl inspect wfcdb-deployment-59c5948c94-bqkmp
kubectl get pods
kubectl describe wfcdb-deployment-59c5948c94-bqkmp
kubectl describe wfcdb-de
kubectl describe pod wfcdb-deployment-59c5948c94-bqkmp
shutdown now
ls
zip .
sudp apt install zip
sudo apt install zip
cd ..
ls
zip -r pfropfen
zip -r pfropfen.zip pfropfen 
sudo zip -r pfropfen.zip pfropfen 
ls
python -m http.server
python3 -m http.server
ls
sudo rm pfropfen.zip
cd pfropfen
ls
shutdown now
ls
sudo nano push.sh
ps
psa
killall
sudo docker image ls
psa
ls
bash push.sh
sudo nano push.sh
sudo docker login -u pfropfen
bash push.sh
ls
cd services
ls
cd ..
mv /services/wfcdeploy.yaml ./wfcdeploy.yaml
mv ./services/wfcdeploy.yaml ./wfcdeploy.yaml
sudo mv ./services/wfcdeploy.yaml ./wfcdeploy.yaml
cd services
ls
cd ..
ls
sudo nano wfcdeploy.yaml 
sudo nano push.sh
bash push.sh
kubectl get nodes
kubectl get pods
kubectl delete -f wfcdeploy.yaml 
killall
kubectl apply -f wfcdeploy.yaml 
kubectl get pods
kubectl descripe pod wfcworker-deployment-698b67bc79-kd
kubectl describe pod wfcworker-deployment-698b67bc79-kd
kubectl describe pod wfcworker-deployment-698b67bc79-kdktx
kubectl describe pod wfcworker-deployment-698b57bc79-kdktx
kubectl logs pod wfcworker-deployment-698b57bc79-kdktx
kubectl logs wfcworker-deployment-698b57bc79-kdktx
cd services
cd worker
ls
sudo nano wavefunctionlookup.py
sudo nano dockerfile
sudo nano Dockerfile
sudo nano wavefunctionlookup.py
sudo nano Dockerfile
cd ..
cd distributor/
ls
sudo nano Dockerfile
cd ..
kuibectl get pods
kubectl get pods
kubectl logs wfchub
kubectl logs wfchub-deployment-c9f57b5b7-vjl78
cd hub
cd services/hub
sudo nano hub.py
sudo nano Dockerfile
cd ..
kubectl get pods
kubectl wfcmanager-deployment-f66898d57-p2zr8
kubectl logs wfcmanager-deployment-f66898d57-p2zr8
cd services/manager
sudo nano manager.py 
sudo nano Dockerfile
cd ..
cd hub
sudo nano Dockerfile
cd ..
cd distributor/
sudo nano Dockerfile
cd ..
ls
cd worker
sudo nano Dockerfile
cd ../..
kubectl get pods
kubectl delete -f wfcdeploy.yaml 
killall
killimg

killimg
killall
kubectl get pods
sudo docker image ls
killimg
sudo docker image ls
brc
ls
sudo docker image ls
brc
killimg
psa
sudo docker image ls
kubectl get pods
killimg
sudo docker image ls
sudo docker image rm -f $(sudo docker image ls)
sudo docker image ls
brc
kubectl get pods
sudo docker image ls
psa
bash build.sh
bash push.sh
kubectl get nodes
kubectl get pods
shutdown now
psa
kubectl get nodes
kubectl get pods
kubectl apply -f wfcdeploy.yaml 
kubectl get pods
kubectl logs wfcdistributor-deployment-7d766d6d7d-9lj4g
cd services/distributor/
sudo nano distributor.py
cd ../..
sudo nano /services/distributor/distributor.py
sudo nano services/distributor/distributo
kubectl logs wfcdistributor-deployment-7d766d6d7d-9lj4g
sudo nano services/distributor/distributor.py
kubectl logs wfcdistributor-deployment-7d766d6d7d-9lj4g
sudo nano services/distributor/distributor.py
sudo nano services/distributor/wavefunctionlookup.py 
sudo nano services/distributor/distributor.py
sudo nano services/worker/wavefunctionlookup.py 
psa
kubectl delete -f wfcdeploy.yaml 
ls
sudo nano rebirth.sh
brc
shutdown now
rebirth
sudo nano rebirth.sh
rebirth
sudo nano rebirth.sh
kubectl get pods

kubectl get pods
kubectl logs wfcdistributor-deployment-7d766d6d7d-nb254
sudo nano services/distributor/wavefunctionlookup.py 
kubectl logs wfcdistributor-deployment-7d766d6d7d-nb254
sudo nano services/manager/manager.py 
sudo nano wfcdeploy.yaml 
kubectl logs wfcdistributor-deployment-7d766d6d7d-nb254
sudo nano wfcdeploy.yaml 
kubectl delete -f wfcdeploy.yaml 
kubectl get pods
kubectl delete -f wfcdeploy.yaml 
kubectl get pods
kubectl apply -f wfcdeploy.yaml 
sudo nano wfcdeploy.yaml 
kubectl get pods
kubectl delete -f wfcdeploy.yaml 
kubectl get pods
kubectl apply -f wfcdeploy.yaml 
sudo nano wfcdeploy.yaml 
kubectl get pods
kubectl delete -f wfcdeploy.yaml
kubectl get pods
kubectl delete --all deployments
kubectl delete --all pods
kubectl get pods
kubectl delete --all
kubectl delete --all pods
kubectl get pods
psa
cd services
ls
sudo nano db/db.py
cd db
ls
cd ..
ls
sudo nano distributor/distributor.py
sudo nano distributor/wavefunctionlookup.py 
c d..
cd ..
sudo nano rebirth.sh 
rebirth
kubectl get pods
sudo nano rebirth.sh
kubectl delete -f wfcdeploy.yaml --namespace=wfc
kubectl delete -f wfcdeploy.yaml --namespace="wfc"
kubectl apply -f wfcdeploy.yaml
kubectl get pods
kubectl get nodes
kubectl get pods
kubectl logs wfcworker-deployment-698b57bc79-b4kww
sudo nano services/distributor/distributor.py 
kubectl get pods
kubectl logs wfcdistributor-deployment-7d766d6d7d-8lmxf
kubectl delete -f wfcdeploy.yaml
sudo nano services/hub/hub.py
sudo nano services/distributor/wavefunctionlookup.py 
sudo nano services/worker/wavefunctionlookup.py 
sudo nano services/worker/worker.py 
sudo nano rebirth.sh 
kubectl get pos
kubectl get pods
kubectl delete --all pods --grace-period=0 --force
kubectl get pods
sudo nano rebirth.sh 
kubectl get pods -A
rebirth
kubectl cluster -info
kubectl cluster-info
kubectl get pods -o wide

kubectl cluster-info
kubectl get pods -o wide
sudo nano wfcdeploy.yaml
kubectl delete -f wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml 
kubectl delete -f wfcdeploy.yaml 
sudo nano wfcdeploy.yaml
kubectl apply -f wfcdeploy.yaml 
kubectl delete -f wfcdeploy.yaml 
sudo nano wfcdeploy.yaml
kubectl apply -f wfcdeploy.yaml 
kubectl get pods -o wide
kubectl logs wfcworker-deployment-698b57bc79-dstcs
kubectl get pods -o wide
kubectl exec --stdin --tty wfcdb-deployment-6fc5bcf544-m669m
kubectl exec --stdin --tty wfcdb-deployment-6fc5bcf544-m669m -- /bin/bash
kubectl delete -f wfcdeploy.yaml 
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml 
kubectl get pods -o wide
kubectl delete -f wfcdeploy.yaml 
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml 
kubectl get pods -o wide
kubectl exec --stdin --tty wfcdb-deployment-6 -- /bin/bash
kubectl get pods -o wide
kubectl exec --stdin --tty wfcdb-deployment-6fc5bcf544-frz9m -- /bin/bash
kubectl get pods -o wide
kubectl exec --stdin --tty wfcdb-deployment-6fc5bcf544-frz9m -- /bin/bash
kubectl delete -f wfcdeploy.yaml
kubectl delete --all deployments
kubectl delete --all pods
kubectl delete --all pods --force
kubectl get pods 
kubectl get pods -A
psa
shutdown now
kubectl get nodes
kubectl get pods
kubectl apply -f wfcdeploy.yaml
kubectl get pods -o wide
kubectl delete -f wfcdeploy.yaml
shutdown now
cd services
ls
cd distributor/
lx
ls
sudo nano distributor.py
cd ../..
ls
cd ..
ls
zip pfropfen
zip /pfropfen
zip v14.zip /pfropfen 
zip pfropfen.zip /pfropfen 
zip v14.zip /pfropfen/* 
ls
zip v14.zip pfropfen
sudo zip v14.zip pfropfen
ls
python3 -m http.server
sudo rm v14.zip
ls
sudo zip v14.zip ./pfropfen
python3 -m http.server
ls
sudo rm v14.zip 
sudo zip -r v14.zip pfropfen
python3 -m http.server
cd pfropfen/services/distributor/
ls
sudo nano distributor.py 
ls
sudo nano wave.py
ls
sudo nano wavefunctionlookup.py 
sudo nano wave.py
ls
cd ..
ls
cd hub
ls
sudo nano hub.py 
ls
cd ..
ls
cd worker
sudo nano worker.py 
cd ..
cd distributor/
sudo nano distributor.py 
sudo nano wave.py
cd ..
cd worker
sudo nano wave.py
s
ls
cd ..
ls
cd ..
kubectl get nodes
psa
kubectl get pods
kubectl get pods -A
ls
rebirth
kubectl get pods
kubectl logs wfchub-dep
kubectl logs wfchub-deployment-c9f57b5b7-6h44j
kubectl get pods
kubectl logs wfcworker-deployment-698b57bc79-7k2zr
cd services
cd distributor/
sudo nano distributor.py 
sudo nano wave.py
cd ..
cd worker
sudo nano worker.py 
sudo nano wave.py 
rebirth
cd ..
rebirth
kubectl get pods
kubectl logs wfcworker-deployment-698b57bc79-hdlkz
cd services/worker
sudo nano worker.py 
sudo nano wave.py 
ls
cd ..
ls
cd ..
ls
sudo nano build.sh
sudo nano push.sh
kubectl get pods
sudo nano rebirth.sh
kubectl get pods
bash push.sh
kubectl get pods
sudo nano wfcdeploy.yaml 
ifconfig
kubectl get pods
kubectl logs wfcdistributor-deployment-7d766d6d7d-rjqf8
kubectl desrcibe wfcdistributor-deployment-7d766d6d7d-rjqf8
kubectl describe wfcdistributor-deployment-7d766d6d7d-rjqf8
kubectl get pods
kubectl describe wfcdistributor-deployment-7d766d6d7d-rjqf8
kubectl logs wfcdistributor-deployment-7d766d6d7d-rjqf8
brc
kubectl delete -f wfcdeploy.yaml
shutdown now
kubectl get pods 
kubectl delete -f wfcdeploy.yaml
kubectl get nodes
kubectl get pods 
kubectl apply -f wfcdeploy.yaml
kubectl get pods 
kubectl get pods -o wide
sudo nano wfcdeploy.yaml 
kubectl delete -f wfcdeploy.yaml
sudo nano wfcdeploy.yaml 
sudo nano rebirth.sh 
kubectl apply -f wfcdeploy.yaml --namespace=wfc
sudo nano rebirth.sh 
sudo nano wfcdeploy.yaml 
psa
killimg
sudo docker image ls
cd services
ls
cd distributor/
sudo nano distributor.py 
cd ..
cd  ..
ls
sudo zip v15.zip -r pfropfen
python3 -m http.server
cd pfropfen
rebirth
kubectl apply -f wfcdeploy.yaml
kubectl get pods
kubectl delete -f wfcdeploy.yaml
sudo nanp wfcdeploy.yaml 
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml --nodeport-addresses=192.168.1.0/24
kubectl apply -f wfcdeploy.yaml --namespace=wfc
kubectl apply -f wfcdeploy.yaml --namespace="wfc"
kubectl create namespace wfc
kubectl get namespaces
kubectl apply -f wfcdeploy.yaml --namespace=wfc
kubectl get pods
kubectl get pods -o wide
kubectl get pods --namespace=wfc
sudo nano wfcdeploy.yaml 
kubectl get svc
kubectl get svc -o wide
sudo nano wfcdeploy.yaml 
kubectl delete -f wfcdeploy.yaml --namespace=wfc
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml
kubectl get svc -o wide
kubectl get pods
kubectl get svc -o wide
kubectl describe service wfcdistributor
curl http://localhost:31001/
curl http://localhost:31001
curl http://localhost:31001/mapGenerator
curl http://127.0.0.1:31001/
curl http://127.0.0.1:31001/mapGenerator
curl 10.10.162.114:5001
kubectl get pods
sudo nano wfcdeploy.yaml 
kubectl delete -f wfcdeploy.yaml 
sudo nano wfcdeploy.yaml 
kubectl delete namespace wfc
kubectl get namespaces
kubectl apply -f wfcdeploy.yaml 
kubectl get pods
kubectl get pods -o wide
kubectl get services
curl http://localhost:31001
curl http://192.168.1.93:31001
curl https://192.168.1.93:31001
kubectl apply -f wfcdeploy.yaml 
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml 
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml 
kubectl get pods
kubectl get pods -o wide
kubectl get services
kubectl svc
kubectl get svc
ifconfig
sudo nano wfcdeploy.yaml 
kubectl apply -f wfcdeploy.yaml 
kubectl get services
sudo nano wfcdeploy.yaml 
kubectl get services
kubectl get pods -o wide
kubectl get services
sudo nano wfcdeploy.yaml 
kubectl delete --all deployments
kubectl delete --all pods
kubectl delete -f wfcdeploy.yaml 
kubectl cluster-info
kubectl get pods 
kubectl create namespace wfc
kubectl apply -f wfcdeploy.yaml --namespace=wfc
kubectl get namespaces
kubectl delete namespace wfc
kubectl create namespace wfc2
kubectl apply -f wfcdeploy.yaml --namespace=wfc2
kubectl get pods -o wide --namespace=wfc
kubectl get pods -o wide --namespace=wfc2
kubectl describe pod wfcdistributor-deployment-7d766d6d7d-5mzpd
kubectl describe pod wfcdistributor-deployment-7d766d6d7d-5mzpd --namespace=wfc2
sudo nano k8install.sh
python3 -m http.server
shutdown now
