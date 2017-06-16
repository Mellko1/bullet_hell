import pygame
from Engine import Engine
from GameScreen import GameScreen
from MenuScreen import MenuScreen
from GameoverScreen import GameoverScreen

pygame.init()
pygame.display.set_caption("Bullet Hell")

img = pygame.image.load("data/new_bullet.png")
pygame.display.set_icon(img)


size = width, height = 800, 600
engine = Engine()
engine.setResolution(size)
engine.registerScreen('Menu', MenuScreen(engine))
engine.registerScreen('Gameplay', GameScreen(engine))
engine.registerScreen('Gameover', GameoverScreen(engine))

engine.setActiveScreen('Menu')

engine.mainLoop()


