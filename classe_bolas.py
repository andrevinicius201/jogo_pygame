import random
import pygame


imagens = ['bola_boliche.jpg','bola_futebol.jpg','bola_volei.jpg','bola_footbal.jpg','bola_basquete.jpg','bola_baseball.jpg','bola_tenis.jpg']
tipos = ['boliche','futebol', 'volei','footbal','basquete','baseball','tenis']
bolas = []

class Bola:
    def __init__(self, x, y, index, vel):
        self.img = pygame.image.load(imagens[index])
        self.tipo = tipos[index]
        self.rect = pygame.Rect(x, y, 20, 20)
        self.vel = vel

def iniciar_bolas():        
    for i in range(50):
        bolas.append(Bola(random.randint(0, 930), random.randint(-1800, 0), random.randint(0, len(imagens)-1), random.randint(3, 8)))

