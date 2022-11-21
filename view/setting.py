import pygame
import sys

"""Базовые настройки игры"""
W = 600
H = 800

FPS = 60

font_name = pygame.font.match_font('arial')

clock = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Battle stars")
