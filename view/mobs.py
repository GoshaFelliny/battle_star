import random
from view.graphix import *


class Mob(pygame.sprite.Sprite):
    """Противник"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mobs_img
        self.rect = self.image.get_rect()
        self.radius = 16
        # отображение хитбоксов pygame.draw.circle(self.image, 'red', self.rect.center, self.radius)
        self.rect.x = random.randrange(W - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        """поведение метеоритов"""
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 20:
            self.rect.x = random.randrange(W - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
