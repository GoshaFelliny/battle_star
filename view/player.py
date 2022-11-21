from view.graphix import *


class Player(pygame.sprite.Sprite):
    """Спрайт игрока"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.radius = 20
        # отображение хитбоксов pygame.draw.circle(self.image, 'red', self.rect.center, self.radius)
        self.rect.centerx = W / 2
        self.rect.bottom = H - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        """Поведение игрока"""
        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx

        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8

        self.rect.y += self.speedy

        if self.rect.right > W:
            self.rect.right = W
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > H:
            self.rect.bottom = H
        if self.rect.top < 0:
            self.rect.top = 0
