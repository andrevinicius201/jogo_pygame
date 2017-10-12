import random
import pygame


imagens = ['bola_boliche.jpg','bola_futebol.jpg','bola_volei.jpg','bola_footbal.jpg','bola_basquete.jpg']
tipos = ['boliche','futebol', 'volei','footbal','basquete']
bolas = []

class Bola:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.img = pygame.image.load(imagens[index])
        self.tipo = tipos[index]
        
for i in range(1500):
    bolas.append(Bola(random.randint(0, 930), random.randint(-18000, 0), random.randint(0, len(imagens)-1)))


