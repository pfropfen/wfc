#!/bin/bash

# Werte für X definieren – diese kannst du anpassen
WORKER_COUNTS=(1 2 4 8 9 16 18 25 32 36 49 50 64 72 98 100 128 144 196 256)

# Deployment-Name und Namespace
DEPLOYMENT_NAME="wfcworker-deployment"
NAMESPACE="default"
POD_LABEL_SELECTOR="app=wfcworker"  # Label anpassen falls nötig

# Passwort einmalig abfragen
read -s -p "Bitte gib dein sudo-Passwort ein: " SUDO_PASSWORD
echo

run_with_sudo() {
    echo "$SUDO_PASSWORD" | sudo -S "$@"
}

wait_for_pods_running() {
    local expected_count=$1
    echo "Warte, bis $expected_count Pods mit Status 'Running' aktiv sind..."

    while true; do
        running_count=$(kubectl get pods -n "$NAMESPACE" -l "$POD_LABEL_SELECTOR" \
            --field-selector=status.phase=Running \
            --no-headers 2>/dev/null | wc -l)

        if [[ "$running_count" -eq "$expected_count" ]]; then
            echo "Alle $expected_count Pods sind 'Running'."
            break
        fi

        echo "Aktuell '$running_count' von '$expected_count' Pods 'Running' – warte 5 Sekunden..."
        sleep 5
    done

    echo "Warte zusätzlich 60 Sekunden für Broker-Registrierung..."
    sleep 60
}

# Hauptdurchlauf
for X in "${WORKER_COUNTS[@]}"; do
    echo "==> Skaliere $DEPLOYMENT_NAME auf $X Worker..."
    kubectl scale deployment "$DEPLOYMENT_NAME" --replicas="$X" -n "$NAMESPACE"

    wait_for_pods_running "$X"

    echo "==> Führe messen.py mit X=$X aus..."
    run_with_sudo python3 messen.py "$X"

    echo "==> Durchlauf für X=$X abgeschlossen."
    echo
done

echo "Alle Durchläufe abgeschlossen."
