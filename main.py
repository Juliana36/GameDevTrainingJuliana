import pygame
import sys
import config

pygame.init()


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
            config.tela = pygame.display.set_mode((config.largura, config.altura), pygame.RESIZABLE)

    # Preenche o fundo da tela com a cor escolhida
    config.tela.fill(config.background_color)

    # Atualiza o conteúdo da tela
    pygame.display.flip()

# Encerra o pygame corretamente
pygame.quit()
sys.exit()