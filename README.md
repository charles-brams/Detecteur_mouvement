# Détecteur de Mouvement avec Raspberry Pi et Caméra

Ce projet utilise un **Raspberry Pi**, un **capteur de mouvement PIR** et une **caméra** pour détecter les mouvements et capturer des images automatiquement.

## Matériel requis
- Raspberry Pi (Modèle 4B ou autre)
- Module Caméra pour Raspberry Pi
- Capteur de Mouvement PIR (HC-SR501)
- Câbles de connexion

## Schéma de connexion
- **VCC** du capteur PIR ➔ **5V** du Raspberry Pi
- **GND** du capteur PIR ➔ **GND** du Raspberry Pi
- **OUT** du capteur PIR ➔ **GPIO 17** du Raspberry Pi

## Utilisation
1. Lorsqu'un mouvement est détecté, une photo est prise et sauvegardée sous le nom **IMG_YYYYMMDD-HHMMSS.jpg**.
2. Le programme continue la surveillance jusqu'à interruption.

## Sauvegarde des images
Les images capturées seront stockées dans le dossier où se trouve le script.

📂 **Dépôt GitHub** : [Lien vers le dépôt](https://github.com/TonNomGitHub/detecteur_mouvement_rpi)

