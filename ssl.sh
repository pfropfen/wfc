#!/bin/bash
#htpasswd -Bbc /root/auth/htpasswd root password
#cat /root/auth/htpasswd

#openssl ecparam -name prime256v1 -genkey -noout -out /certs/server.key
#openssl req -new -sha256 -key /certs/server.key -out /certs/server.csr

#openssl req -newkey rsa:4096 -nodes -sha256 -keyout /certs/server.key -x509 -days 365 -out /certs/server.crt

sudo docker run -d --rm -p 9000:443 -v /root/auth/:/opt/auth -v /root/certs/:/opt/certs -e REGISTRY_HTTP_ADDR=0.0.0.0:443 -e REGISTRY_HTTP_TLS_CERTIFICATE=/opt/certs/server.crt -e REGISTRY_HTTP_TLS_KEY=/opt/certs/server.key -e REFISTRY_AUTH=htpasswd -e REGISTRY_AUTH_HTPASSWD_REALM=Registry-Realm -e REGISTRY_AUTH_HTPASSWD_PATH=/opt/auth/htpasswd --name registry2 registry:2


