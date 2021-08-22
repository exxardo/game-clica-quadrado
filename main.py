import pygame

pygame.init()

# em pixels
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode(largura_tela, altura_tela)

terminou = False
while not terminou:
    # Atualizar o desenho na tela:
    pygame.display.update()

    # Checar os eventos do mouse:
    for evento in pygame.event.get():
        


pygame.quit()