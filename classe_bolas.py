import random
import pygame


imagens = ['bola_boliche.jpg','bola_futebol.jpg','bola_volei.jpg','bola_footbal.jpg','bola_basquete.jpg','bola_baseball.jpg','bola_tenis.jpg',"gold.png"]
tipos = ['boliche','futebol', 'volei','footbal','basquete','baseball','tenis','dourada']
bolas = []
dourada = []

class Bola:
    def __init__(self, x, y, index, vel):
        self.img = pygame.image.load(imagens[index])
        self.tipo = tipos[index]
        self.rect = pygame.Rect(x, y, 20, 20)
        self.vel = vel

def iniciar_bolas():        
    for i in range(30):
        bolas.append(Bola(random.randint(0, 930), random.randint(-1800, 0), random.randint(0, len(imagens)-2), random.randint(3, 5)))


def cair_dourada():        
    for i in range(1):
        bolas.append(Bola(random.randint(0, 930), random.randint(-1800, 0), 7, random.randint(3, 5)))
