import pygame
import sys

pygame.init()

#configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE) # pygame.RESIZABLE é uma flag que permite  usuário redimensione a janela (amplie ou reduza) ao arrastar suas bordas.

#Imagens de Fundo
imagem_fundo = pygame.image.load("IMAGENS/fundo/blackground.JPEG")




