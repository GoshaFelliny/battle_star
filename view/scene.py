from view.sprites import *
from view.graphix import *
from view.setting import *
import pygame_textinput
from BaseDate.orm import *


def lose_show():
    """Сцена во время проигрыша"""
    screen.blit(background, background_rect)
    draw_text(screen, 'Игра завершена, нажмите пробел', 30, W / 2, 100)
    Hight = 200

    # Вывод таблицы лидеров
    for players in BasePlayer.select().order_by(BasePlayer.score.desc()).limit(5):
        draw_text(screen, f' {players.name}:  {players.score}', 35, 200, Hight)
        Hight += 100

    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                waiting = False


def main_scene():
    """Сцена во время запуска"""

    manager = pygame_textinput.TextInputManager(validator=lambda input: len(input) <= 5)

    textinput = pygame_textinput.TextInputVisualizer(manager=manager, font_object=pygame.font.SysFont("Consolas", 55))

    wait = True

    while wait:
        screen.blit(background, background_rect)
        draw_text(screen, 'Battle Star!', 40, W / 2, H / 3)
        draw_text(screen, 'Движение с помощью стрелок', 23, W / 2, 400)
        draw_text(screen, "Стрельба с помозью пробела", 23, W / 2, 450)
        draw_text(screen, 'Введите имя и нажмите "Enter"', 24, W / 2, 750)

        textinput.cursor_color = (255, 255, 255)
        textinput.antialias = False
        textinput.font_color = 'white'

        events = pygame.event.get()

        textinput.update(events)
        screen.blit(textinput.surface, (220, 600))
        pygame.display.flip()

        for event in events:
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return textinput.value
