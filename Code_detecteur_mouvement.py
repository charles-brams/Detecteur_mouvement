import RPi.GPIO as GPIO  # Importation de la bibliothèque pour contrôler les GPIO du Raspberry Pi
from picamera import PiCamera  # Importation de la bibliothèque pour contrôler la caméra du Raspberry Pi
import time  # Bibliothèque pour gérer le temps et les pauses
from datetime import datetime  # Permet d'obtenir l'heure et la date actuelles

# Configuration du mode de numérotation des broches du Raspberry Pi
GPIO.setmode(GPIO.BCM)

# Définition du numéro de broche du capteur PIR
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)  # Configuration de la broche en entrée pour lire les signaux du capteur PIR

# Initialisation de la caméra
camera = PiCamera()

try:
    time.sleep(5)  # Pause de 5 secondes

    while True: 
        if GPIO.input(PIR_PIN):  # Vérifie si le capteur PIR détecte un mouvement
            
            print("Motion Detected!")  # Affiche un message dans la console
            
            # Génération d'un nom de fichier
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            image_name = 'IMAGE_' + timestamp + '.jpg'
            
            camera.start_preview()  # Active la caméra
            time.sleep(2)  # Pause de 2 secondes 
            camera.capture(image_name)  # Capture et enregistre l'image
            camera.stop_preview()  # Désactive la caméra
            
            time.sleep(2)  # Pause de 2 secondes

        time.sleep(1)  # Pause d'une seconde avant de vérifier à nouveau le capteur

except KeyboardInterrupt:  # Si l'utilisateur interrompt le programme
    print("Quit")  # Affiche un message de sortie
    GPIO.cleanup()  # Réinitialise les broches GPIO pour éviter tout problème lors de la prochaine exécution