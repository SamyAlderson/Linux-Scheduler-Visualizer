"""
Module qui collecte les données de planification à intervalles réguliers.

Ce module utilise le module psutil pour récupérer les informations sur les processus
et les tâches en cours d'exécution. Les données sont stockées dans un fichier CSV
pour une analyse ultérieure.

"""

import psutil
import pandas as pd
import time
import logging

# Configuration du logger
logging.basicConfig(level=logging.INFO)

def collect_data(interval: int = 1) -> None:
    """
    Collecte les données de planification à intervalles réguliers.

    Args:
    - interval (int): Intervalle de temps en secondes entre chacune des collectes.
    - logging_interval (int): Intervalle de temps en secondes entre chacune des
      impressions de logs.

    Raises:
    - ValueError: Si l'intervalle est inférieur à 1.

    """
    if interval < 1:
        raise ValueError("L'intervalle doit être supérieur ou égal à 1")

    while True:
        # Récupération des informations sur les processus
        process_info = []
        for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent']):
            process_info.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'status': proc.info['status'],
                'cpu_percent': proc.info['cpu_percent']
            })

        # Récupération des informations sur les tâches
        task_info = []
        for task in psutil.tasks():
            task_info.append({
                'pid': task.pid,
                'name': task.name(),
                'status': task.status(),
                'cpu_percent': task.cpu_percent()
            })

        # Stockage des données dans un fichier CSV
        data = pd.DataFrame(process_info + task_info)
        data.to_csv('data.csv', index=False, mode='a', header=(not data.empty))

        # Impression de logs
        logging.info(f"Collecte des données à {time.time()}")

        # Attente de l'intervalle suivant
        time.sleep(interval)

def main() -> None:
    """
    Exécution du module.

    """
    try:
        # Collecte des données à intervalles réguliers
        collect_data()
    except KeyboardInterrupt:
        # Arrêt de la collecte des données
        logging.info("Arrêt de la collecte des données")

if __name__ == "__main__":
    main()