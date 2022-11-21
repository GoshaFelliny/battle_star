import pygame.event
from view.scene import *
from BaseDate.orm import *


def start():
    name = ""
    score = 0

    for i in range(15):
        new_mobs()

    run = True

    lose = False
    menu = True

    while run:
        if menu:
            name = main_scene()
            menu = False
        if lose:
            for mob in mobs:
                mob.kill()
            lose_show()
            lose = False
            menu = True
            player.rect.bottom = H - 10
            score = 0
            all_sprites.draw(screen)
            for _ in range(15):
                new_mobs()

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot()

        all_sprites.update()

        # столкновение метиорита и пули
        mobs_hits = pygame.sprite.groupcollide(bullets, mobs, True, True)
        for _ in mobs_hits:
            score += 1
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        # столкновение метиорита и игрока
        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
        if hits:
            lose = True
            add_record(name=name, score=score)

        screen.blit(background, background_rect)
        all_sprites.draw(screen)

        # вывод очков
        draw_text(screen, str(score), 18, W / 2, 10)

        pygame.display.flip()
