import pygame

def main():
    pygame.init()
    tela = pygame.display.set_mode([600, 400])
    pygame.display.set_caption("Soccer Game Escape")
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_azul = (108,194,236)
    cor_verde = (152,231,114)
    cor_vermelha = (227,57,9)
    cor_rosa = (253,147,226)

    ret = pygame.Rect(10, 10, 45, 45)
    
    sair = False

    pygame.font.init()

    font_padrao = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(font_padrao, 45)
    fonte_ganhou = pygame.font.SysFont(font_padrao, 30)

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(150,150)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                ret = ret.move(10,10)

            if event.type == pygame.MOUSEMOTION:
                ret = ret.move(-1,-1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ret.move_ip(-10,0)
                    
                if event.key == pygame.K_RIGHT:
                    ret.move_ip(10,0)
                    
                if event.key == pygame.K_UP:
                    ret.move_ip(0,-10)
                    
                if event.key == pygame.K_DOWN:
                    ret.move_ip(0,10)

                if event.key == pygame.K_SPACE:
                    ret.move_ip(10,10)

                if event.key == pygame.K_BACKSPACE:
                    ret.move_ip(-10,-10)           
                 
                
        relogio.tick(30)
        tela.fill(cor_branca)

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2

        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.display.update()
    pygame.quit()
    
    

main()
    

