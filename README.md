# MONITOR DE RECURSOS DO COMPUTADOR

#### Sobre:

O programa tem como função o monitoramente e exibição dos recursos presentes no computador. Ele se utiliza dos seguintes módulos e ferramentas: pygame, psutil, py-cpuinfo e platform.
Tais módulos juntos confere ao programa uma boa visualização do consumo de memória ram, a utilização do processador, do armazenado, além de apresentar informações referentes a nomeclatura do processador, a versão do sistema operacional e o endereço de IP da máquina.

Capturas de tela:

![PRINT 1](https://github.com/exxardo/assets/blob/main/Print%201%20-%20Monitor%20recursos.png)

![PRINT 2](https://github.com/exxardo/assets/blob/main/Print%202%20-%20Monitor%20recursos.png)

![PRINT 3](https://github.com/exxardo/assets/blob/main/Print%203%20-%20Monitor%20recursos.png)

----

#### Sobre os módulos e ferramentas utilizados:

##### `pygame`: Pygame é uma biblioteca de jogos que utlizamos em conjunto com o Python. Utilizamos esse módulo para criar a interface gráfica do programa: a janela, as barras de nível e a plotagem das informações na janela. A plotagem das informações na janela se deu através do usode um recurso do pygame chamado: surface. Surfaces são as superfícies em 2D (que podem ser também 3D) onde se desenha o as informções, podendo preencher uma área com uma cor ou mudar a cor da superfície dependendo da posição, e outros recursos.

Exemplo do uso da surface:
```PYTHON
# Superficies de plotagem dos marcadores de consumo: preto e vermelho
superficie_1 = pygame.surface.Surface((largura_tela, altura_tela / 3))
superficie_2 = pygame.surface.Surface((largura_tela, altura_tela / 3))
superficie_3 = pygame.surface.Surface((largura_tela, altura_tela / 3))
```

##### `psutil`: Psutil é uma biblioteca de plataforma cruzada para recuperar informações sobre os processos em execução e a utilização do sistema como CPU, memória, discos, rede e sensores em Python. É útil no monitoramento de sistema. Utilizamos o psutil na captura das informações referentes ao uso da memória, ao uso do procesador e no monitoramente do memória de armazenamento.

Podemos ver o uso do Psutil na seguinte função:

```PYTHON
def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2 * 20
    tela.blit(superficie_3, (0, 2 * altura_tela/3)) # Superficies
    pygame.draw.rect(superficie_3, preto, (20, 0, largura_tela-2*20, 70)) # Superficies
    larg = larg * disco.percent / 100
    pygame.draw.rect(superficie_3, vermelho, (20, 0, larg, 70)) # Superficies
    
    total = round(disco.total / (1024 * 1024 * 1024), 2)
    usado = round(disco.used / (1024 * 1024 * 1024), 2)
    disponivel = round(disco.free / (1024 * 1024 * 1024), 2)
    texto_barra = f'Amazenamento Total: {total} GB | Disponível: {disponivel} GB | Utilizado: {usado} GB ({disco.percent}%)'
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 370))
```

##### `cpuinfo`: Py-cpuinfo obtém informações da CPU, como nomeclatura, núcleos, etc. utilizando o Python puro. Neste projeto ele foi usado apenas para capturar a nomeclatura comercial do processador. 

Como vemos na terceira linha da função `mostra_uso_cpu()`: 

```PYTHON
def mostra_uso_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    info = cpuinfo.get_cpu_info() # Nomeclatura do processador
    nome = info['brand_raw'] # Nomeclatura do processador
    larg = largura_tela - 2 * 20
    tela.blit(superficie_2, (0, altura_tela/3)) # Superficies
    pygame.draw.rect(superficie_2, preto, (20, 20, largura_tela-2 * 20, 70)) # Superficies
    larg = larg * capacidade / 100
    pygame.draw.rect(superficie_2, vermelho, (20, 20, larg, 70)) # Superficies
    text = font.render(f'Utilização de CPU: {capacidade}% | {nome}', 1, branco)
    tela.blit(text, (20, 190))
``` 

##### `platform`: Com este móduto é possível obter características do processador, como o nome e modelo. Além disso, estão disponíveis também informações sobre o sistema operacional. Utilizamos ele para capturar informações do nome real do processador e a versão do sistemas operacional.

Exemplo de utilização em duas funções:

```PYTHON
# Mais informações
    # Info do processador
def datalhar_processador():
    processador = platform.processor()
    text = font.render(processador, 1, branco)
    tela.blit(text, (20, 520))
    
    # Info da versão do sistema
def datalhar_plataforma():
    plataforma = platform.platform()
    text = font.render(plataforma, 1, branco)
    tela.blit(text, (20, 540))
```

----

#### Sobre o IP:

Um endereço IP é uma representação numérica de onde um dispositivo está conectado à internet. Serve para identificar onde está um dispositivo e a natureza desse dispositivo. O Internet Protocol (IP) é um conjunto de regras para comunicação pela internet.
O endereço IP pode identificar seu próprio computador, um site favorito, um servidor de rede e até mesmo um dispositivo, como webcam.
Os endereços IP são importantes para enviar e receber informações. Eles direcionam tráfego de internet para onde é necessário.

---
