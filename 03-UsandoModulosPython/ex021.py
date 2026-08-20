import pygame

pygame.init()
pygame.mixer_music.load("data/Saiba-DUAS-COISAS.mp3")
pygame.mixer_music.play()
pygame.event.wait()
input("Parar a música?")
