# Linux Scheduler Visualizer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/username/projet/actions/workflows/main.yml/badge.svg)](https://github.com/username/projet/actions/workflows/main.yml)

## Description

L'outil de visualisation de la politique de planification du noyau Linux permet de visualiser les données de planification en temps réel. Il utilise l'interface graphique pour afficher les données de planification, les processus et les threads en cours d'exécution.

## Fonctionnalités

* Récupération des données de planification en temps réel
* Affichage des données de planification dans un graphique
* Suivi des processus et des threads en cours d'exécution
* Possibilité de filtrer les données de planification par processus ou par thread

## Installation

Pour installer l'outil, assurez-vous d'avoir Python 3.8 ou supérieur installé sur votre système. Vous pouvez installer les dépendances nécessaires en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

## Usage

Pour lancer l'outil, exécutez la commande suivante :

```bash
python src/main.py
```

Vous pouvez alors accéder à l'interface graphique en vous connectant à l'adresse `http://localhost:8080` dans votre navigateur.

## Architecture du projet

Le projet est composé de cinq modules principaux :

* `src/main.py` : Gère l'interface utilisateur et la récupération des données de planification
* `src/scheduler.py` : Module qui interagit avec le noyau Linux pour récupérer les données de planification
* `src/visualizer.py` : Module qui gère la visualisation des données de planification
* `src/datacollector.py` : Module qui collecte les données de planification à intervalles réguliers
* `docs/README.md` : Document de base du projet

## Contribuer

Pour contribuer au projet, créez un fork du projet et soumettez vos modifications comme pull request. Assurez-vous de suivre les conventions de codage et les standards de qualité.

## Licence

Ce projet est régi par la licence MIT. Vous pouvez trouver plus d'informations sur la licence [ici](https://opensource.org/licenses/MIT).