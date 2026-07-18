"""
Module qui interagit avec le noyau Linux pour récupérer les données de planification
"""

import psutil
import os
import time
from typing import Dict, List

class Scheduler:
    """
    Classe qui gère l'interaction avec le noyau Linux pour récupérer les données de planification
    """

    def __init__(self):
        """
        Initialisation de la classe
        """
        self.processes = {}
        self.last_update = time.time()

    def get_processes(self) -> Dict[int, Dict[str, str]]:
        """
        Récupère les informations des processus actuellement exécutés

        Returns:
            Dict[int, Dict[str, str]]: Dictionnaire des processus avec leurs informations
        """
        try:
            return {p.pid: {
                "name": p.name(),
                "cpu_percent": p.cpu_percent(),
                "memory_percent": p.memory_percent()
            } for p in psutil.process_iter() if p.is_running()}
        except psutil.Error as e:
            print(f"Erreur lors de la récupération des processus : {e}")
            return {}

    def get_scheduler_info(self) -> Dict[str, str]:
        """
        Récupère les informations de la politique de planification

        Returns:
            Dict[str, str]: Dictionnaire des informations de la politique de planification
        """
        try:
            with open("/proc/schedstat", "r") as f:
                lines = f.readlines()
                return {"scheduler_info": lines[-1].strip()}
        except FileNotFoundError as e:
            print(f"Erreur lors de la récupération des informations de la politique de planification : {e}")
            return {}

    def update(self):
        """
        Met à jour les données de planification
        """
        self.processes = self.get_processes()
        self.last_update = time.time()

    def get_data(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Récupère les données de planification

        Returns:
            Dict[str, List[Dict[str, str]]]: Dictionnaire des données de planification
        """
        return {
            "processes": self.processes,
            "scheduler_info": self.get_scheduler_info(),
            "last_update": self.last_update
        }

def main():
    """
    Fonction principale qui gère l'interaction avec le noyau Linux
    """
    scheduler = Scheduler()
    scheduler.update()
    data = scheduler.get_data()
    print(data)

if __name__ == "__main__":
    main()