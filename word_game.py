"""
Nom : Blanc
Prenom : John Clayton
Date : 11 Avril 2021

   Images: Background et Movement
"""
import sys
from pygame import mixer
import pygame
from random import random

pygame.init()  # initialisé le module Pygame

mots = ['papa', 'maman', 'fille', 'avocat', 'electricien', 'plombier', 'manger', 'jouer', 'football', 'salon']


# Fonction choisisant les mots par hasard
def choisir():
    position_mot = int(random() * 10)
    mot = mots[position_mot]
    return mot


compteur_de_tentative = 0
score = 0
lettres_devinees_en_erreur = ''

mot_a_afficher = ''
mot_choisi = choisir()

for i in range(len(mot_choisi)):
    mot_a_afficher = mot_a_afficher + "-"


def jeu_devine_mot(lettre, mot):
    global score

    joindre = ''
    mot_a_devine = []

    for i in mot:
        mot_a_devine.append(i)
    if mot_a_devine.count("-") > 0:
        i = mot_choisi.find(lettre)
        if i > -1:
            # Son agréable
            ding_sound = pygame.mixer.Sound('audios\\ding.wav')
            ding_sound.play()

            while i > -1:
                score += 100 / len(mot)
                mot_a_devine[i] = lettre
                i = mot_choisi.find(lettre, i + 1)
        else:
            # Son désagréable
            ding_sound = pygame.mixer.Sound('audios\\miss.wav')
            ding_sound.play()

            global lettres_devinees_en_erreur
            lettres_devinees_en_erreur += lettre
            score -= 2

        for i in mot_a_devine:
            joindre = joindre + i
        return joindre


# The GUI
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # dimension de l'écran

# Set background
background_img = pygame.image.load("images/images.png")

# Set caption
pygame.display.set_caption('Université Espoir de Calvary Chapel')

# Set icon
icon = pygame.image.load('images/dove.png')  # size about 5x5 pixels
pygame.display.set_icon(icon)

clock = pygame.time.Clock()  # utilisé pour fréquence d'affichage
base_font = pygame.font.Font(None, 32)  # font ou police: defaut et size : 32

font_color = (0, 150, 250)
font_obj = pygame.font.Font("C:\\Windows\\Fonts\\segoeprb.ttf", 25)

# Render the objects
text_obj1 = font_obj.render("Bienvenue au Jeu de Mots Simple", True, font_color)
text_obj2 = font_obj.render("Déjà devinées :", True, font_color)

# Définir dimension des boites
input_rect = pygame.Rect(230, 110, 180, 40)
rectangle = pygame.Rect(200, 200, 250, 40)


def main():
    color = pygame.Color('white')
    global compteur_de_tentative
    global mot_a_afficher
    global score
    global mot_choisi
    mot = mot_a_afficher
    message_perdu = ""
    message_gagne = ""
    message_score = ""

    # sound
    mixer.music.load('audios/background.wav')
    mixer.music.play(-1)  # -1 means loop play

    while True:
        # sorte de nettoyage
        screen.blit(background_img, (0, 0))

        # display LABEL
        screen.blit(text_obj1, (int(WIDTH / 2) - int(text_obj1.get_rect().width / 2), 0))
        screen.blit(text_obj2, (10, 205))

        pygame.draw.rect(screen, color, input_rect, 0)
        pygame.draw.rect(screen, color, rectangle, 0)

        tirets = base_font.render(mot, True, (0, 0, 0))
        screen.blit(tirets, (input_rect.x + 5, input_rect.y + 10))

        text_label = base_font.render(lettres_devinees_en_erreur, True, (0, 0, 0))
        screen.blit(text_label, (205, 205))

        message1 = font_obj.render(message_perdu, True, font_color)
        screen.blit(message1, (150, 290))
        message2 = font_obj.render(message_gagne, True, font_color)
        screen.blit(message2, (150, 290))
        message3 = font_obj.render(message_score, True, font_color)
        screen.blit(message3, (170, 340))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # autres clés
            if event.type == pygame.KEYDOWN:
                if compteur_de_tentative == 20:
                    message_perdu = ">> Vous avez perdu ! <<"
                    message_score = f"Votre score est: {score}"
                    mixer.music.stop()
                    break

                if mot_a_afficher == mot_choisi:
                    message_gagne = ">> Vous avez gagne ! <<"
                    message2 = font_obj.render(message_gagne, True, font_color)
                    screen.blit(message2, (150, 290))
                    message_score = f"Votre score est: {score}"
                    mixer.music.stop()
                    break

                lettre = event.unicode

                mot_a_afficher = jeu_devine_mot(lettre, mot_a_afficher)
                compteur_de_tentative += 1
                mot = mot_a_afficher

        # refresh écran
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
