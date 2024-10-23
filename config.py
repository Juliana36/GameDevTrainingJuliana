import pygame
import sys

pygame.init()

#configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE) # pygame.RESIZABLE é uma flag que permite  usuário redimensione a janela (amplie ou reduza) ao arrastar suas bordas.
background_color = (0, 0, 255)  # define a cor da tela para azul



