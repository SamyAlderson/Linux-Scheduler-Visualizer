"""
Fichier src/main.py

Gère l'interface utilisateur et la récupération des données de planification.

Auteur: Your Name
Date: today
"""

import sys
import argparse
from src.scheduler import Scheduler
from src.visualizer import Visualizer
from src.datacollector import DataCollector
from src.utils import get_logger

# Configuration du logging
logger = get_logger(__name__)

def main():
    """
    Programme principal.
    """
    parser = argparse.ArgumentParser(description="Linux Scheduler Visualizer")
    parser.add_argument("-c", "--config", help="Fichier de configuration")
    args = parser.parse_args()

    # Instanciation de l'objet Scheduler
    scheduler = Scheduler()

    # Lancement du collecteur de données
    data_collector = DataCollector(scheduler)
    data_collector.start()

    # Instanciation de l'objet Visualizer
    visualizer = Visualizer(scheduler)

    # Lancement du visualiseur
    visualizer.start()

    # Boucle d'attente infinie
    while True:
        pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Arrêt manuel du programme")
    except Exception as e:
        logger.error(f"Erreur : {e}")
        sys.exit(1)
```

```python
"""
Fichier src/scheduler.py

Module qui interagit avec le noyau Linux pour récupérer les données de planification.

Auteur: Your Name
Date: today
"""

import psutil

class Scheduler:
    """
    Classe qui représente une politique de planification.
    """

    def __init__(self):
        """
        Initialisation de l'objet Scheduler.
        """
        self.process_list = []

    def get_process_list(self):
        """
        Récupère la liste des processus en cours d'exécution.
        """
        return psutil.process_iter()

    def update_process_list(self):
        """
        Met à jour la liste des processus en cours d'exécution.
        """
        self.process_list = self.get_process_list()
```

```python
"""
Fichier src/visualizer.py

Module qui gère la visualisation des données de planification.

Auteur: Your Name
Date: today
"""

import matplotlib.pyplot as plt

class Visualizer:
    """
    Classe qui représente un visualiseur de données.
    """

    def __init__(self, scheduler):
        """
        Initialisation de l'objet Visualizer.
        """
        self.scheduler = scheduler

    def start(self):
        """
        Lancement du visualiseur.
        """
        self.plot_process_list()

    def plot_process_list(self):
        """
        Affiche la liste des processus en cours d'exécution.
        """
        plt.bar([p.pid for p in self.scheduler.process_list], [p.cpu_percent() for p in self.scheduler.process_list])
        plt.xlabel('PID')
        plt.ylabel('CPU Utilisation')
        plt.title('Processes List')
        plt.show()
```

```python
"""
Fichier src/datacollector.py

Module qui collecte les données de planification à intervalles réguliers.

Auteur: Your Name
Date: today
"""

import time
from src.scheduler import Scheduler

class DataCollector:
    """
    Classe qui représente un collecteur de données.
    """

    def __init__(self, scheduler):
        """
        Initialisation de l'objet DataCollector.
        """
        self.scheduler = scheduler
        self.data = {}

    def start(self):
        """
        Lancement du collecteur de données.
        """
        while True:
            self.collect_data()
            time.sleep(1)

    def collect_data(self):
        """
        Collecte les données de planification.
        """
        self.data = {p.pid: p.cpu_percent() for p in self.scheduler.get_process_list()}
```

```python
"""
Fichier src/utils.py

Module qui contient des fonctions utilitaires.

Auteur: Your Name
Date: today
"""

import logging

def get_logger(name):
    """
    Récupère un objet logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger