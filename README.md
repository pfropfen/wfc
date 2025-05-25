# Projektname

Parallelisierung des Wave Function Collapse Algorithmus in einem Kubernetes Cluster


## Zweck

Dieses Projekt wurde im Rahmen einer Masterarbeit im Studiengang Informatik erstellt und dient dazu, innerhalb eines
Kubernetes Clusters mit Hilfe verschiedener Dienste digitale Landkarten unter Verwendung des Wave Function Collapse Algorithmus 
zu generieren.


## Voraussetzungen

* Ein oder mehrere Computer mit einem Linux Betriebssystem (durchgeführt und getestet wurde das Projekt mit Ubuntu Server 22.04 LTS,
  sowie Ubuntu Server 24.04 LTS). Falls ein Computer verwendet wird können Virtuelle Maschinen genutzt werden. Empfohlen wird, mindestens
  3 Maschinen (1 Master/Manager + 2 Nodes) zu verwenden.

* Webbrowser

* Um generierte Landkarten zu visualisieren, wird ein beliebiges Betriebssystem (Windows, MacOS, Linux) benötigt auf dem folgende
Applikationen installiert sind:
	- Python
	- Python Requests
	- Python Pygame
	- Python Pandas
	

## Installation und Betrieb

Auf der Master-Node:
git clone https://github.com/pfropfen/wfc.git  # das Repository klonen
sudo bash k8master.sh                          # im Ordner wfc das Skript ausführen, Kubernetes wird vollständig installiert und konfiguriert

Anschließend muss die Datei "jointoken.sh" über beliebigen Weg auf alle zu verwendenden Nodes transferriert werden.


Auf der Worker-Node (gilt für jede Maschine einzeln):
git clone https://github.com/pfropfen/wfc.git  # das Repository klonen
sudo bash k8node.sh							   # im Ordner wfc das Skript ausführen, Kubernetes wird vollständig installiert und konfiguriert

Nachdem die Datei "jointoken.sh" von der Master-Node übertragen wurde:
sudo bash jointoken.sh                         # die Node wird dem Cluster hinzugefügt


Auf der Master-Node:
kubectl apply -f wfcdeploy.yaml				   # um das Deployment auszurollen
kubectl delete -f wfcdeploy.yaml			   # um das Deployment zu stoppen

kubectl get nodes                              # um den Status aller Nodes abzufragen
kubectl get pods                               # um den Status aller Pods abzufragen
kubectl get pods -o wide 					   # um den Status aller Pods inklusive der Zuordnung zu Nodes abzufragen


Über einen Webbrowser können nun folgende Adressen erreicht werden:
http://[MASTER-NODE-IP]:31000/setRules         # Manager Service um Rules festzulegen (Mapgröße, Anzahl Abschnitte, Entropietoleranz)
http://[MASTER-NODE-IP]:31001/mapGenerator     # Distributor Service um einen Generierungsprozess anzustoßen, am Ende der Generierung wird die MapID auf der Seite ausgegeben


Worker während des Betriebs skalieren:

kubectl scale deployment/wfcworker-deployment --replicas=1


Für die Maploader Applikation muss maploader.py sowie wavefunctionlookup.py einmalig angepast werden indem die IP der Master-Node der Variablen "managerurl" zugewiesen wird.
Für die Timeextractor Applikation muss timex.py ebenfalls angepasst werden in dem bei export_database_to_csv(host="XXX.XXX.XX.XX",..) die IP der Manager-Node eingetragen wird.  
 
Um eine generierte Map anzeigen zu lassen:
maploader.py ausführen und MapID eingeben.

Um die gemessenen Zeiten abzurufen:
timex.py ausführen.


