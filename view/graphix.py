from os import path
from view.setting import *

"""Файлы спрайтов"""
src_dir = path.join(path.dirname(__file__), 'src')
background = pygame.image.load(path.join(src_dir, 'background.bmp')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(src_dir, "player_img.png")).convert()
mobs_img = pygame.image.load(path.join(src_dir, "mobs_img.png")).convert()