import pygame
from Engine import Engine
from GameScreen import GameScreen
from MenuScreen import MenuScreen
from GameoverScreen import GameoverScreen

pygame.init()

size = width, height = 800, 600
engine = Engine()
engine.setResolution(size)
engine.registerScreen('Menu', MenuScreen(engine))
engine.registerScreen('Gameplay', GameScreen(engine))
engine.registerScreen('Gameover', GameoverScreen(engine))

engine.setActiveScreen('Menu')

engine.mainLoop()


