# Linux Scheduler Visualizer
==========================

Un outil de visualisation de la politique de planification du noyau Linux.

## Présentation

Ce projet est un outil de visualisation de la politique de planification du noyau Linux. Il permet d'afficher en temps réel la politique de planification, de visualiser la charge de travail des processus, d'analyser la durée d'exécution des processus et de comparer différentes politiques de planification.

## Fichier du projet

Ce projet est composé de 5 fichiers :

* `src/main.py` : Gère l'interface utilisateur et la récupération des données de planification.
* `src/scheduler.py` : Module qui interagit avec le noyau Linux pour récupérer les données de planification.
* `src/visualizer.py` : Module qui gère la visualisation des données de planification.
* `src/datacollector.py` : Module qui collecte les données de planification à intervalles réguliers.
* `docs/README.md` : Document de base du projet.

## Fonctionnalités

Ce projet offre les fonctionnalités suivantes :

* Affichage en temps réel de la politique de planification
* Visualisation de la charge de travail des processus
* Analyse de la durée d'exécution des processus
* Comparaison de différentes politiques de planification

## Dépendances

Ce projet nécessite les bibliothèques suivantes :

* `python`
* `psutil`
* `matplotlib`
* `pandas`

## Langage

Ce projet est écrit en `python`.

## Domaine

Ce projet est lié au domaine du noyau Linux.