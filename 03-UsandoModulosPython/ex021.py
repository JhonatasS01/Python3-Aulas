import pygame

pygame.init()
pygame.mixer_music.load("date/Saiba-DUAS-COISAS.mp3")
pygame.mixer_music.play()
pygame.event.wait()
input("Parar a música?")
