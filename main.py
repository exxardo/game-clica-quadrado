import pygame
import pygame.time

#Iniciando o pygame:
pygame.init()

# Dimensões da tela em pixels:
largura_tela = 800
altura_tela = 600

# Configurando tamanho da tela:
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Desenhando os retangulos
    # Definição das cores:
cor = (255, 255, 0)
area = (100, 100, 30, 30)
pygame.draw.rect(tela, cor, area)

cor = (255, 0, 0)
area = (200, 200, 30, 30)
pygame.draw.rect(tela, cor, area)

clock = pygame.time.Clock()

terminou = False
while not terminou:
    # Atualizar o desenho na tela:
    pygame.display.update()

    # Configura 60 atualizações de tela por segundo:
    clock.tick(60)

    # Checar os eventos do mouse:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

# Finaliza a tela:
pygame.display.quit()

# Finalizando o pygame:
pygame.quit()