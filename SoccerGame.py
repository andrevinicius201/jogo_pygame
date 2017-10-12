import pygame, sys
import random
import classe_bolas

def main():
    pygame.init()
    tela = pygame.display.set_mode([950, 587])
    pygame.display.set_caption("Soccer Game Escape")
    relogio = pygame.time.Clock()
    
    cor_branca = (255, 255, 255)
    
    cont = 0
    
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

    def jogadorAcertouUmaBola(retJogador, bolas):
        for b in bolas:
            if retJogador.colliderect():
                return True
        return False


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

            '''if event.type == pygame.MOUSEBUTTONDOWN:
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
                    retJogador.move_ip(0,10)'''      

                
        for bola in range(len(classe_bolas.bolas)):
            tela.blit(classe_bolas.bolas[bola].img, (classe_bolas.bolas[bola].x, classe_bolas.bolas[bola].y))
            classe_bolas.bolas[bola].y += 5

            if classe_bolas.bolas[bola].y > 620:
                classe_bolas.bolas[bola].y = -18000
                cont += 1

            pos = pygame.mouse.get_pos()

            if pos[0] == (classe_bolas.bolas[bola].x + 15) and pos[1] == (classe_bolas.bolas[bola].y+15):
                sair = True
                break
                

                                    
        pygame.display.update()               
        
        tela.blit(imagem_fundo, (0, 0))
               
        (retJogador.left, retJogador.top) = pygame.mouse.get_pos()

        pos = pygame.mouse.get_pos()
        
        
        if pos[0] > 900:
            pygame.mouse.set_pos(900,pos[1])
            
        elif pos[1] > 540:
            pygame.mouse.set_pos(pos[0],540)
                    
        pygame.mouse.set_visible(0)
        
        tela.blit(imagemJogador, retJogador)       

        relogio.tick(60)
        
    pygame.quit()
    
    

main()
    

