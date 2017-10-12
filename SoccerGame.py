import pygame, sys
import random
import classe_bolas

def main():
    pygame.init()
    tela = pygame.display.set_mode([1100, 680])
    pygame.display.set_caption("Soccer Game Escape")
    relogio = pygame.time.Clock()
    cor_branca = (255, 255, 255)

    #boliche = pygame.image.load("bola_boliche.jpg")

    '''boliche = [0,0]

    for i in range(2):
        boliche[i] = pygame.image.load("bola_boliche.jpg")'''

    #bolas = [boliche,futebol,volei]
    

    def encerrar():
        pygame.quit()

    def apertarAlgumaTecla():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    encerrar()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        encerrar()
                    return


    def desenharTexto(text, font, surface, x, y):
        textobj = font.render(text, 1, cor_branca)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


    pygame.font.init()

    font = pygame.font.SysFont(None, 48)

    desenharTexto('Soccer Game Escape', font, tela, 400, 225)
    desenharTexto('Press a key to start.', font, tela, 400 - 30, 225 + 50)
    pygame.display.update()
    apertarAlgumaTecla()

    imagem_fundo = pygame.image.load("campo.jpg")

    imagemJogador = pygame.image.load("messi.jpg")
    retJogador = imagemJogador.get_rect()
    
    sair = False

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                retJogador = retJogador.move(10,10)

            if event.type == pygame.MOUSEMOTION:
                retJogador = retJogador.move(-1,-1)
            
            if event.type == pygame.KEYDOWN:
                if event.key == ord('a'):
                    retJogador = (retJogador[0]+10, retJogador[1], retJogador[2], retJogador[3])
                    print("de boas")
                    
                if event.key == ord('d'):
                    retJogador.move_ip(10,0)
                    
                if event.key == ord('w'):
                    retJogador.move_ip(0,-10)
                    
                if event.key == ord('s'):
                    retJogador.move_ip(0,10)        

        '''cont_bolas = 0
        
        if cont_bolas < 15:
            aleatorio = random.randint(0,15)
            for i in range(aleatorio):
                ale = random.randint(0,49)
                tela.blit(classe_bolas.bolas[ale].img, (classe_bolas.bolas[ale].x, classe_bolas.bolas[ale].y))
                classe_bolas.bolas[ale].y += 5
                cont_bolas += 1
            if classe_bolas.bolas[ale].y > 690:
                cont_bolas -= 1
                print("caralho")'''

        todas_bolas = []
        
        cont_bolas = 0

        while cont_bolas < 15:
            ale = random.randint(0,49)
            bola = [classe_bolas.bolas[ale].img, (classe_bolas.bolas[ale].x, classe_bolas.bolas[ale].y)]
            todas_bolas.append(bola)
            cont_bolas += 1

        for bola in todas_bolas:
            tela.blit(bola[0],bola[1])

        
            
        pygame.display.update()               
        
        tela.blit(imagem_fundo, (0, 0))
        
        
        (retJogador.left, retJogador.top) = pygame.mouse.get_pos()

        pos = pygame.mouse.get_pos()
        
        
        if pos[0] > 1050:
            pygame.mouse.set_pos(1050,pos[1])
            

        elif pos[1] > 610:
            pygame.mouse.set_pos(pos[0],610)
            
        
        pygame.mouse.set_visible(0)
        

        tela.blit(imagemJogador, retJogador)
        
        #pygame.display.update()
        

        relogio.tick(40)
        
    pygame.quit()
    
    

main()
    

