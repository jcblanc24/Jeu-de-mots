import pygame
import pygame_menu
import sys

pygame.init()
surface = pygame.display.set_mode((600, 400))


def start_the_game():
    import word_game


menu = pygame_menu.Menu(
    height=400,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=600
)


menu.add.button("Play", start_the_game)
menu.add.button("Quit", pygame_menu.events.EXIT)

menu.mainloop(surface)
