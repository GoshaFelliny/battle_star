from view.mobs import *
from view.player import *
from view.bullets import *


"""
Группировка и отрисовка спрайтов 
"""

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()

bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


# новые мобы
def new_mobs():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


# отрисовка стрельбы
def shoot():
    bullet = Bullet(player.rect.centerx, player.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)


# вывод текста
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, 'white')
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
