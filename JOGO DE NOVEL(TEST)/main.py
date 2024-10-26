import pygame
import sys
import config

pygame.init()

config.imagem_fundo = pygame.transform.scale(config.imagem_fundo, (config.largura, config.altura))
# Loop principal do jogo
running = True
while running:
    # Processa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Atualiza as dimensões da tela quando a janela é redimensionada
            config.largura, config.altura = event.w, event.h
            config.tela = pygame.display.set_mode((config.largura, config.altura), pygame.RESIZABLE)#para abrir a janela
            config.imagem_fundo = pygame.transform.scale(config.imagem_fundo, (config.largura, config.altura))#para fazer a imagem de fundo ser redimensionada conforme a redimensão da tela.
           


            #Para ver a posição do mouse
        fonte = pygame.font.Font(None, 36)
        mouse_x, mouse_y = pygame.mouse.get_pos() #capitura a posição do mouse.
        text = fonte.render(f"Posição: ({mouse_x}, {mouse_y})", True, (0, 0, 0))

    

    config.tela.blit(config.imagem_fundo, (0,0))
    config.tela.blit(text, (10,10)) #printa a posição do mouse na tela. 

    # Atualiza o conteúdo da tela
    pygame.display.flip()

# Encerra o pygame corretamente
pygame.quit()
sys.exit()