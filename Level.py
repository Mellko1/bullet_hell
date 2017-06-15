import pygame

class Level:

    startTime = 0
    currentTime = 0
    passedSeconds = 0
    spawned = 0

    def __init__(self):
        self.startTime = 0
        self.currentTime = 0
        pass

    # spawnowanie przeciwnikow co okreslony czas, mozna ustawic teksture, pozycje startowa, kierunek, typ strzalu
    def update(self, _clock, _enemyList, _gameViewRect, _gameView, _player, _engine):
        pass


