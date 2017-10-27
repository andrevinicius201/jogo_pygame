import pygame, sys
import random
import classe_bolas
import time

def main():
    pygame.init()
    tela = pygame.display.set_mode([950, 587])
    pygame.display.set_caption("Soccer Game Escape")
    relogio = pygame.time.Clock()    
    cor_branca = (255, 255, 255)
        
    
    def encerrar():
        pygame.quit()
        sys.exit()

    def apertarAlgumaTecla():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    encerrar()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        encerrar()
                    sair1 = False
                    return sair1
                if event.type == pygame.MOUSEBUTTONUP:
                    sair1 = False
                    return sair1 
            
                
    def desenharTexto(text, font, surface, x, y):
        textobj = font.render(text, 1, cor_branca)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    pygame.font.init()

    font = pygame.font.SysFont("comicsansms", 40)
    fonte = pygame.font.SysFont("times", 36)

    imagem_inicio = pygame.image.load("img_inicio.jpg")
    imagem_final = pygame.image.load("img_final.jpg")

    tela.blit(imagem_inicio,(0,0))
    desenharTexto('Soccer Game Escape', font, tela, 310, 225)
    desenharTexto('Pressione alguma tecla para começar', font, tela, 150, 275)
    desenharTexto('Pegue apenas as bolas de futebol. ', fonte, tela, 150, 320)
    desenharTexto('Caso precise pausar o jogo a ', fonte, tela, 150,350)
    desenharTexto('qualquer momento, pressione P', fonte, tela, 150,400)
    pygame.display.update()
    apertarAlgumaTecla()

    imagem_fundo = pygame.image.load("campo.jpg")

    imagemJogador = pygame.image.load("messi.jpg")
    retJogador = imagemJogador.get_rect()

    topScore = 0
    sair = False
    contador = 0
    while sair != True:
        contador += 1
        print(contador)
        score = 0
        
        sair1 = False

        classe_bolas.bolas = []
        classe_bolas.iniciar_bolas()
        pygame.mouse.set_pos(500,500)

        dificuldade = 10
        
        while sair1 != True:
            tela.blit(imagem_fundo, (0, 0))
            tela.blit(imagemJogador, retJogador)
            
            desenharTexto('Score: %s' % (score), font, tela, 10, 0)
            desenharTexto('Top Score: %s' % (topScore), font, tela, 10, 40)

            (retJogador.left, retJogador.top) = pygame.mouse.get_pos()

            position = pygame.mouse.get_pos()
            
            if position[0] > 900:
                pygame.mouse.set_pos(900,position[1])
                
            elif position[1] > 540:
                pygame.mouse.set_pos(position[0],540)
                        
            pygame.mouse.set_visible(0)

            for b in classe_bolas.bolas:
                tela.blit(b.img, b.rect)

            pygame.display.update()
                                                               
            for b in classe_bolas.bolas:
                b.rect.move_ip(0,b.vel)

            for b in classe_bolas.bolas[:]:
                if b.rect.top > 600:
                    classe_bolas.bolas.remove(b)
                    classe_bolas.bolas.append(classe_bolas.Bola(random.randint(0, 930), random.randint(-1800, 0), random.randint(0, len(classe_bolas.imagens)-1), random.randint(3, 5)))
            
            for b in classe_bolas.bolas:
                if retJogador.colliderect(b.rect):
                    if b.tipo == 'futebol':
                        score += 1
                        classe_bolas.bolas.remove(b)
                        classe_bolas.bolas.append(classe_bolas.Bola(random.randint(0, 930), random.randint(-1800, 0), random.randint(0, len(classe_bolas.imagens)-1), random.randint(3, 5)))
                    elif b.tipo != 'futebol':
                        if score > topScore :
                            topScore = score
                        classe_bolas.quant = 50
                        sair1 = True

            if score == dificuldade:
                dificuldade += 10
                for i in range(5):
                    classe_bolas.bolas.append(classe_bolas.Bola(random.randint(0, 930), random.randint(-1800, 0), random.randint(0, len(classe_bolas.imagens)-1), random.randint(3, 5))) 
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair1 = True                   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:                        
                        sair1 = True
                    elif event.key == pygame.K_p:
                        relogio.tick(1000000000000)

            
            relogio.tick(60)
       
        tela.blit(imagem_final, (0,0))
        desenharTexto('GAME OVER', font, tela, 380, 60)
        desenharTexto('Pressione uma tecla para jogar novamente', font, tela, 100, 110)
        pygame.display.update()        
        apertarAlgumaTecla()
    
main()
    

