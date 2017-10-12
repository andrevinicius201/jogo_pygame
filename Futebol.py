import pygame, random, sys
from pygame.locals import *

telaLarg = 1100
telaAlt = 680
corTexto = (255, 255, 255)
FPS = 40
bolaTamMin = 30
bolaTamMax = 50
bolaVelMin = 1
bolaVelMax = 6
addNovaBola = 6
movimentoJoga = 5

def encerrar():
    pygame.quit()
    sys.exit()

def apertarAlgumaTecla():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                encerrar()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    encerrar()
                return

def jogadorAcertouUmaBola(retJogador, bolas):
    for b in bolas:
        if b['img'] == '<Surface(30x32x32 SW)>':
            print("beleza")
        if retJogador.colliderect(b['rect']):
            return True
    return False

def desenharTexto(text, font, surface, x, y):
    textobj = font.render(text, 1, corTexto)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

pygame.init()
mainClock = pygame.time.Clock()
tela = pygame.display.set_mode((telaLarg, telaAlt))
pygame.display.set_caption('Futebol Escape')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 48)

imgJogador = pygame.image.load('messi.jpg')
retJogador = imgJogador.get_rect()

imgFundo = pygame.image.load('campo.jpg')

desenharTexto('Futebol Escape', font, tela, (telaLarg / 3), (telaAlt / 3))
desenharTexto('Pressione uma tecla para começar.', font, tela, (telaLarg / 3) - 30, (telaAlt / 3) + 50)
pygame.display.update()
apertarAlgumaTecla()


topScore = 0
while True:
    bolas = []
    score = 0
    retJogador.topleft = (telaLarg / 2, telaAlt - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    bolaAddContador = 0

    while True:
        todas_bolas = ["bola_boliche.jpg","bola_futebol.jpg","bola_volei.jpg"]
        imgBola = pygame.image.load(todas_bolas[random.randint(0,2)])
        #imgBola = pygame.image.load('bola_futebol.jpg')
        

        score += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                encerrar()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    encerrar()
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            if event.type == MOUSEMOTION:
                retJogador.move_ip(event.pos[0] - retJogador.centerx, event.pos[1] - retJogador.centery)

        if not reverseCheat and not slowCheat:
            bolaAddContador += 1
            
        if bolaAddContador == addNovaBola:
            bolaAddContador = 0
            bolaTam = random.randint(bolaTamMin, bolaTamMax)
            novaBola = {'rect': pygame.Rect(random.randint(0, telaLarg-bolaTam), 0 - bolaTam, bolaTam, bolaTam),
                        'speed': random.randint(bolaVelMin, bolaVelMax),
                        'surface':pygame.transform.scale(imgBola, (bolaTam, bolaTam)),
                        'img': imgBola
                        }
            
            bolas.append(novaBola)     

        if moveLeft and retJogador.left > 0:
            retJogador.move_ip(-1 * movimentoJoga, 0)
        if moveRight and retJogador.right < telaLarg:
            retJogador.move_ip(movimentoJoga, 0)
        if moveUp and retJogador.top > 0:
            retJogador.move_ip(0, -1 * movimentoJoga)
        if moveDown and retJogador.bottom < telaAlt:
            retJogador.move_ip(0, movimentoJoga)

        pygame.mouse.set_pos(retJogador.centerx, retJogador.centery)

        for b in bolas:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        for b in bolas[:]:
            if b['rect'].top > telaAlt:
                bolas.remove(b)

        tela.blit(imgFundo,(0,0))

        desenharTexto('Score: %s' % (score), font, tela, 10, 0)
        desenharTexto('Top Score: %s' % (topScore), font, tela, 10, 40)

        tela.blit(imgJogador, retJogador)

        for b in bolas:
            tela.blit(b['surface'], b['rect'])

        pygame.display.update()

        if jogadorAcertouUmaBola(retJogador, bolas):            
            if score > topScore:
                topScore = score
            break

        mainClock.tick(FPS)

    desenharTexto('GAME OVER', font, tela, (telaLarg / 3), (telaAlt / 3))
    desenharTexto('Pressione uma tecla para jogar novamente.', font, tela, (telaLarg / 3) - 80, (telaAlt / 3) + 50)
    pygame.display.update()
    apertarAlgumaTecla()
