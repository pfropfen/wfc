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

### Auf der Manager-Node:

```bash
# Repository klonen
git clone https://github.com/pfropfen/wfc.git  

# Kubernetes installieren und konfigurieren
sudo bash k8master.sh                          
```
Anschließend muss die Datei "jointoken.sh" über einen beliebigen Weg auf alle zu verwendenden Nodes transferriert werden.


### Auf jeder Worker-Node:

```bash
# Repository klonen
git clone https://github.com/pfropfen/wfc.git  

# Kubernetes installieren und konfigurieren
sudo bash k8node.sh
```
Nachdem die Datei "jointoken.sh" von der Master-Node übertragen wurde:
```bash
# Node zum Cluster hinzufügen
sudo bash jointoken.sh                         
```

### Zurück auf der Manager-Node:

```bash
# Deployment ausrollen
kubectl apply -f wfcdeploy.yaml

# Deployment stoppen
kubectl delete -f wfcdeploy.yaml

# Status der Nodes
kubectl get nodes

# Status der Pods
kubectl get pods

# Status der Pods inklusive Zuordnung zu Nodes
kubectl get pods -o wide

# Worker während des Betriebs skalieren 					   
kubectl scale deployment/wfcworker-deployment --replicas=X
```
Über einen Webbrowser können nun folgende Adressen erreicht werden:
http://[MASTER-NODE-IP]:31000/setRules         # Manager Service um Rules festzulegen (Mapgröße, Anzahl Abschnitte, Entropietoleranz)
http://[MASTER-NODE-IP]:31001/mapGenerator     # Distributor Service um einen Generierungsprozess anzustoßen, am Ende der Generierung wird die MapID auf der Seite ausgegeben


### Visualisierung
Um eine generierte Map zu visualisieren wird die Maploader Applikation verwendet. Diese muss angepasst werden, indem in den Dateien maploader.py sowie wavefunctionlookup.py die IP der Master-Node der Variablen "managerurl" zugewiesen wird.
Um eine generierte Map anzeigen zu lassen: maploader.py ausführen und MapID eingeben.

### Zeiten aus Datenbank exportieren
Für die Timeextractor Applikation muss timex.py ebenfalls angepasst werden in dem bei export_database_to_csv(host="XXX.XXX.XX.XX",..) die IP der Manager-Node eingetragen wird.  
Um gemessene Zeiten abzurufen: timex.py ausführen.

### Messungen durchführen
Um eine Reihe von Messungen automatisiert durchzuführen, wird das Skript messen.py verwendet. Am Anfang der Datei muss für die Variable "BASE_IP" die IP der Manager-Node eingetragen werden. Durch ausführen des Skripts mit einem Argument X werden alle Messungen durchgeführt welche in der Datei messreihen.csv enthalten sind und für die die Anzahl der Worker X beträgt. Die gemessenen Zeiten werden durch das Skript zusammen mit den entsprechenden MapIDs in der CSV-Datei eingetragen. 
Das Skript "messung.sh" kann dazu verwendet werden automatisiert verschiedene Messreihen mit unterschiedlicher Worker-Anzahl durchzuführen. Dazu müssen in der Datei alle Zahlen im Feld "WORKER-COUNTS" aufgelistet werden, mit denen messen.py nacheinander ausgeführt werden soll.


## Monitoring

Über die Adresse http://[MASTER-NODE-IP]:31672 kann das RabbitMQ Management aufgerufen werden. Die Zugangsdaten sind User=guest und Passwort=guest. Dort können in Echtzeit die eingehenden Maptickets sowie die Verbundenen Worker (Consumer) überwacht werden.

Um während der Verwendung des messen.py-Skripts den Status der Kubernetes Pods von einem anderen Rechner aus zu überprüfen muss der Ordner ~/.kube/config der Manager-Node kopiert werden. Anschließend kann mit ```kubectl get pods``` der Status angezeigt werden.
 
