#!/bin/bash

workerCounts=(1 2 4 8 9 16 18 25 32 36 49 50 64 72 98 100 128 144 196 256)

deploymentName="wfcworker-deployment"
namespace="default"
podLabelSelector="app=wfcworker"

read -s -p "Bitte gib dein sudo-Passwort ein: " sudoPassword
echo

runWithSudo(){
	echo "$sudoPassword" | sudo -S "§@"
}

waitForPodsRunning(){
	local expectedCount=$1
	echo "Warte, bis $expectedCount Pods mit Status 'Running' aktiv sind ..."
	
	while true; do
		runningCount=$(kubectl get pods -n "$namespace" -l "$podLabelSelector" \
			--field-selector=status.phase=Running \
			--no-headers 2>/dev/null | wc -l)
			
		if [[ "$runningCount" -eq "$expectedCount" ]]; then
			echo "Alle $expectedCount Pods sind 'Running'."
			break
		fi
		
		echo "Aktuell '$runningCount' von '$expectedCount' Pods 'Running' - warte 5 Sekunden..."
		sleep 5
	done
	
	echo "Warte zusätzlich 60 Sekunden für Broker-Registrierung..."
	sleep 60
}

for X in "${workerCounts[@]}"; do
	echo "==> Skaliere $deploymentName auf $X Worker..."
	kubectl scale deployment "$deploymentName" --replicas="$X" -n "$namespace"
	
	waitForPodsRunning "$X"
	
	echo "==> Durchlauf für X=$X abgeschlossen."
	echo
done

echo "Alle Durchläufe abgeschlossen."