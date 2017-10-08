import pygame

def main():
    pygame.init()
    tela = pygame.display.set_mode([1100, 680])
    pygame.display.set_caption("Soccer Game Escape")
    relogio = pygame.time.Clock()

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
                
        relogio.tick(40)
        
        tela.blit(imagem_fundo, (0, 0))

        (xant, yant) = (retJogador.left, retJogador.top)
        (retJogador.left, retJogador.top) = pygame.mouse.get_pos()
        pygame.mouse.set_visible(0)
        retJogador.left -= retJogador.width/2
        retJogador.top -= retJogador.height/2

        tela.blit(imagemJogador, retJogador)
        pygame.display.update()
    pygame.quit()
    
    

main()
    

