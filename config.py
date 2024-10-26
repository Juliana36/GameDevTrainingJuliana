import pygame
import sys

pygame.init()

#configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE) # pygame.RESIZABLE é uma flag que permite  usuário redimensione a janela (amplie ou reduza) ao arrastar suas bordas.
background_color = (0, 0, 255)  # define a cor da tela para azul

#Para ver a posição do mouse
fonte = pygame.font.Font(None, 36)
mouse_x, mouse_y = pygame.mouse.get_pos() #capitura a posição do mouse.
text = fonte.render(f"Posição: ({mouse_x}, {mouse_y})", True, (255, 255, 255))






