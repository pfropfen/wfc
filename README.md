# Parallelisierung des Wave Function Collapse Algorithmus in einem Kubernetes Cluster




## Dieses Projekt wurde im Rahmen einer Masterarbeit im Studiengang Informatik erstellt und dient dazu, innerhalb eines Kubernetes Clusters mit Hilfe verschiedener Dienste digitale Landkarten unter Verwendung des Wave Function Collapse Algorithmus zu generieren.




## Voraussetzungen

* Ein oder mehrere Computer mit einem Linux Betriebssystem (durchgeführt und getestet wurde das Projekt mit Ubuntu Server 22.04 LTS, sowie Ubuntu Server 24.04 LTS). Falls ein einzelner Computer verwendet wird können Virtuelle Maschinen genutzt werden. Empfohlen wird, mindestens 3 Maschinen (1 Manager + 2 Nodes) zu verwenden.

* Um einen Generierungsprozess zu starten sowie die Parameter für die Generierung festzulegen, wird ein Webbrowser benötigt.

* Um generierte Landkarten zu visualisieren, wird ein beliebiges Betriebssystem (Windows, MacOS, Linux) benötigt auf dem folgende Applikationen installiert sind:
	- Python
	- Python Requests
	- Python Pygame
	- Python Pandas
	

## Installation und Betrieb

Auf der Manager-Node:
git clone https://github.com/pfropfen/wfc.git  # das Repository klonen
sudo bash k8master.sh                          # Kubernetes wird vollständig installiert und konfiguriert

Anschließend muss die Datei "jointoken.sh" über einen beliebigen Weg auf alle zu verwendenden Nodes transferriert werden.


Auf jeder Worker-Node:
git clone https://github.com/pfropfen/wfc.git  # das Repository klonen
sudo bash k8node.sh							   # Kubernetes wird vollständig installiert und konfiguriert

Nachdem die Datei "jointoken.sh" von der Master-Node übertragen wurde:
sudo bash jointoken.sh                         # die Node wird dem Cluster hinzugefügt


Auf der Manager-Node:
kubectl apply -f wfcdeploy.yaml				   # um das Deployment auszurollen
kubectl delete -f wfcdeploy.yaml			   # um das Deployment zu stoppen

kubectl get nodes                              # um den Status aller Nodes abzufragen
kubectl get pods                               # um den Status aller Pods abzufragen
kubectl get pods -o wide 					   # um den Status aller Pods inklusive der Zuordnung zu Nodes abzufragen

kubectl scale deployment/wfcworker-deployment --replicas=X	# Worker während des Betriebs auf X Replicas skalieren

Über einen Webbrowser können nun folgende Adressen erreicht werden:
http://[MASTER-NODE-IP]:31000/setRules         # Manager Service um Rules festzulegen (Mapgröße, Anzahl Abschnitte, Entropietoleranz)
http://[MASTER-NODE-IP]:31001/mapGenerator     # Distributor Service um einen Generierungsprozess anzustoßen, am Ende der Generierung wird die MapID auf der Seite ausgegeben



Um eine generierte Map zu visualisieren wird die Maploader Applikation verwendet. Diese muss angepasst werden, indem in den Dateien maploader.py sowie wavefunctionlookup.py die IP der Master-Node der Variablen "managerurl" zugewiesen wird.
Um eine generierte Map anzeigen zu lassen: maploader.py ausführen und MapID eingeben.

Für die Timeextractor Applikation muss timex.py ebenfalls angepasst werden in dem bei export_database_to_csv(host="XXX.XXX.XX.XX",..) die IP der Manager-Node eingetragen wird.  
Um gemessene Zeiten abzurufen: timex.py ausführen.

Um eine Reihe von Messungen automatisiert durchzuführen, wird das Skript messen.py verwendet. Am Anfang der Datei muss für die Variable "BASE_IP" die IP der Manager-Node eingetragen werden.
Durch ausführen des Skripts mit einem Argument X werden alle Messungen durchgeführt welche in der Datei messreihen.csv enthalten sind und für die die Anzahl der Worker X beträgt.
Das Skript "messung.sh" kann dazu verwendet werden automatisiert verschiedene Messreihen mit unterschiedlicher Worker-Anzahl durchzuführen. Dazu müssen in der Datei alle Zahlen im Feld "WORKER-COUNTS" aufgelistet werden, mit denen messen.py nacheinander ausgeführt werden soll.



