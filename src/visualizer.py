"""
Module src/visualizer.py

Gère la visualisation des données de planification pour le projet Linux Scheduler Visualizer.

Auteur: [Votre nom]
Date: [Aujourd'hui]
"""

import matplotlib.pyplot as plt
import pandas as pd
from src.scheduler import Scheduler

class Visualizer:
    """
    Classe Visualizer

    Gère la visualisation des données de planification.
    """

    def __init__(self, scheduler: Scheduler):
        """
        Constructeur de la classe Visualizer.

        Args:
        scheduler (Scheduler): Objet Scheduler pour récupérer les données de planification.
        """
        self.scheduler = scheduler

    def affiche_politique(self):
        """
        Affiche en temps réel la politique de planification.
        """
        try:
            # Récupère les données de planification
            data = self.scheduler.recupere_donnees_planning()
            # Crée un DataFrame pour les données de planification
            df = pd.DataFrame(data)
            # Affiche le DataFrame
            print(df)
        except Exception as e:
            # Gère les erreurs
            print(f"Erreur : {e}")

    def visualise_charge_de_travail(self):
        """
        Visualise la charge de travail des processus.
        """
        try:
            # Récupère les données de planification
            data = self.scheduler.recupere_donnees_planning()
            # Crée un DataFrame pour les données de planification
            df = pd.DataFrame(data)
            # Crée un graphique pour la charge de travail
            plt.figure(figsize=(10, 6))
            plt.plot(df['temps'], df['charge_de_travail'])
            plt.xlabel('Temps')
            plt.ylabel('Charge de travail')
            plt.title('Charge de travail des processus')
            plt.show()
        except Exception as e:
            # Gère les erreurs
            print(f"Erreur : {e}")

    def analyse_duree_execution(self):
        """
        Analyse la durée d'exécution des processus.
        """
        try:
            # Récupère les données de planification
            data = self.scheduler.recupere_donnees_planning()
            # Crée un DataFrame pour les données de planification
            df = pd.DataFrame(data)
            # Crée un graphique pour la durée d'exécution
            plt.figure(figsize=(10, 6))
            plt.plot(df['temps'], df['duree_execution'])
            plt.xlabel('Temps')
            plt.ylabel('Durée d'exécution')
            plt.title('Durée d'exécution des processus')
            plt.show()
        except Exception as e:
            # Gère les erreurs
            print(f"Erreur : {e}")

    def compare_politiques(self):
        """
        Compare différentes politiques de planification.
        """
        try:
            # Récupère les données de planification
            data = self.scheduler.recupere_donnees_planning()
            # Crée un DataFrame pour les données de planification
            df = pd.DataFrame(data)
            # Crée un graphique pour la comparaison des politiques
            plt.figure(figsize=(10, 6))
            plt.plot(df['temps'], df['politique_1'])
            plt.plot(df['temps'], df['politique_2'])
            plt.xlabel('Temps')
            plt.ylabel('Chargement')
            plt.title('Comparaison des politiques de planification')
            plt.show()
        except Exception as e:
            # Gère les erreurs
            print(f"Erreur : {e}")

def affiche_aide():
    """
    Affiche l'aide pour l'outil de visualisation.
    """
    print("Aide pour l'outil de visualisation :")
    print("affiche_politique : Affiche en temps réel la politique de planification.")
    print("visualise_charge_de_travail : Visualise la charge de travail des processus.")
    print("analyse_duree_execution : Analyse la durée d'exécution des processus.")
    print("compare_politiques : Compare différentes politiques de planification.")

if __name__ == "__main__":
    # Récupère les données de planification
    scheduler = Scheduler()
    visualiser = Visualizer(scheduler)
    affiche_aide()
    action = input("Entrer l'action à effectuer (affiche_politique, visualise_charge_de_travail, analyse_duree_execution, compare_politiques, aide) : ")
    if action == "affiche_politique":
        visualiser.affiche_politique()
    elif action == "visualise_charge_de_travail":
        visualiser.visualise_charge_de_travail()
    elif action == "analyse_duree_execution":
        visualiser.analyse_duree_execution()
    elif action == "compare_politiques":
        visualiser.compare_politiques()
    elif action == "aide":
        affiche_aide()
    else:
        print("Action non reconnue.")
```
