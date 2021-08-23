import pygame
import pygame.time
import random

#Iniciando o pygame:
pygame.init()

# Dimensões da tela em pixels:
largura_tela = 800
altura_tela = 600

# Configurando tamanho da tela:
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Desenhando os retangulos
    # Definição das cores:
    
class quadradinho():
    def __init__(self):
        self.largura = 30
        self.altura = 30
        self.x = random.randint(0, largura_tela - 30)
        self.y = random.randint(0, altura_tela - 30)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = random.randint(20, 255), random.randint(20, 255), random.randint(20, 255) # R, G, B
        
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)
        
classQuadradinho = quadradinho()
classQuadradinho.desenhar(tela)
    
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
