import pygame
import pygame.time
import random

#Iniciando o pygame:
pygame.init()

# Quantidade de quadrados apresentados
quadrados_iniciais = 20

largura_tela = 800 # Em pixels
altura_tela = 600 # Em pixels
preto = (0, 0, 0)
branco = (255, 255, 255)
terminou = False
tempo_inicial = 30 # Segundos
conta_clocks = 0
pontos = 0
conta_segundos = tempo_inicial

# Configurando tamanho da tela:
tela = pygame.display.set_mode((largura_tela, altura_tela))

def mostrar_tempo(tempo, pontos):
    font = pygame.font.Font(None, 24)
    text = font.render(f'Tempo: {tempo}s | Pontuação: {pontos}', 1, branco)
    textpos = text.get_rect(centerx=tela.get_width() / 2)
    tela.blit(text, textpos)
    
def mostrar_pontuacao_final(tela, pontos):
    tela.fill(preto) # Limpar toda a tela
    font = pygame.font.Font(None, 40)
    text = font.render(f'Pontuaçãoo: {pontos}s | Pontuação: {pontos}', 1, branco)
    textpos = text.get_rect(center=(tela.get_width() / 2, tela.get_height() / 2))
                            
clock = pygame.time.Clock()

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
        
lista = []
for desenhar in range(0, quadrados_iniciais):        
    classeQuadradinho = quadradinho()
    classeQuadradinho.desenhar(tela)
    lista.append(classeQuadradinho)

while not terminou:
    # Atualizar o desenho na tela:
    pygame.display.update()

    # Configura 60 atualizações de tela por segundo:
    clock.tick(60)

    # Checar evento de saída:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    
        # Checar evento de clique no quadradinho:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            posicao = pygame.mouse.get_pos()
            for classeQuadradinho in lista:
                if classeQuadradinho.area.collidepoint(posicao):
                    lista.remove(classeQuadradinho)
                    pontos = pontos + 1
                    
    conta_clocks = conta_clocks + 1
    
    if conta_clocks == 60:
        if conta_segundos >= 0:
            conta_segundos = conta_segundos - 1
        conta_clocks = 0
        classeQuadradinho = quadradinho()
        lista.append(classeQuadradinho)
        
    if conta_segundos > 0:
        tela.fill(preto)
        for quadradinho in lista:
            quadradinho.desenhar(tela)
            mostrar_tempo(conta_segundos, pontos)
            
    else:
        mostrar_pontuacao_final(tela, pontos)
        for quadradinho in lista:
            lista.remove(classeQuadradinho)
                             
# Finaliza a tela:
pygame.display.quit()

# Finalizando o pygame:
pygame.quit()
