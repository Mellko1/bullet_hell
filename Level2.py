import pygame
from Level import Level
from Enemy import Enemy, ShootType


class Level2(Level):
    def __init__(self):
        super(Level2, self).__init__()
        pass

    # spawnowanie przeciwnikow co okreslony czas, mozna ustawic teksture, pozycje startowa, kierunek, typ strzalu
    def update(self, _clock, _enemyList, _gameViewRect, _gameView, _player, _engine):
        self.currentTime += _clock.get_time()
        if self.currentTime >= 1000:
            self.passedSeconds += 1
            self.currentTime = 0
            self.spawned = 0

        # warunek konczacy poziom
        if self.passedSeconds == 60 and self.spawned == 0:
            _engine.setActiveScreen('Gameover')
            _engine.lastScore = _player.score
            self.spawned = 1

        if self.passedSeconds == 5 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship5.png", 1, (_gameViewRect.x + _gameViewRect.width / 5, _gameViewRect.y - 50),
                      pygame.math.Vector2(0, 1),
                      ShootType.FOURDIRECTION, 20))
            _enemyList.add(
                Enemy("data/ship5.png", 1, (_gameViewRect.x + _gameViewRect.width * 4 / 5, _gameViewRect.y - 50),
                      pygame.math.Vector2(0, 1),
                      ShootType.FOURDIRECTION, 20))
            self.spawned = 1

        if self.passedSeconds == 10 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/spiked ship 3.png", 1, (_gameViewRect.x + _gameViewRect.width / 4, _gameViewRect.y - 50),
                      pygame.math.Vector2(0, 2),
                      ShootType.DOUBLE, 20))
            _enemyList.add(
                Enemy("data/spiked ship 3.png", 1,
                      (_gameViewRect.x + _gameViewRect.width * 3 / 4, _gameViewRect.y - 50), pygame.math.Vector2(0, 2),
                      ShootType.DOUBLE, 20))
            self.spawned = 1

        if self.passedSeconds == 11 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/spiked ship 3.png", 1, (_gameViewRect.x + _gameViewRect.width / 4, _gameViewRect.y - 50),
                      pygame.math.Vector2(0, 2),
                      ShootType.SPUN, 20))
            _enemyList.add(
                Enemy("data/spiked ship 3.png", 1,
                      (_gameViewRect.x + _gameViewRect.width * 3 / 4, _gameViewRect.y - 50), pygame.math.Vector2(0, 2),
                      ShootType.SPUN, 20))
            self.spawned = 1

        if self.passedSeconds == 12 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/spiked ship 3.png", 1, (_gameViewRect.x + _gameViewRect.width / 4, _gameViewRect.y - 50),
                      pygame.math.Vector2(0, 2),
                      ShootType.DOUBLE, 20))
            _enemyList.add(
                Enemy("data/spiked ship 3.png", 1,
                      (_gameViewRect.x + _gameViewRect.width * 3 / 4, _gameViewRect.y - 50), pygame.math.Vector2(0, 2),
                      ShootType.DOUBLE, 20))
            self.spawned = 1

        if self.passedSeconds == 15 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship5.png", 1, (_gameViewRect.x + _gameViewRect.width / 5, _gameViewRect.y - 50),
                      pygame.math.Vector2(0, 1),
                      ShootType.FOURDIRECTION, 20))
            _enemyList.add(
                Enemy("data/ship5.png", 1, (_gameViewRect.x + _gameViewRect.width * 4 / 5, _gameViewRect.y - 50),
                      pygame.math.Vector2(0, 1),
                      ShootType.FOURDIRECTION, 20))
            self.spawned = 1

        if self.passedSeconds == 20 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship1.png", 1, (_gameViewRect.x + _gameViewRect.width / 2, _gameViewRect.y - 50),
                      pygame.math.Vector2(0, 1),
                      ShootType.EIGHTDIRECTION, 20))
            self.spawned = 1

        if self.passedSeconds == 25 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/spiked ship 3.png", 1, (0, _gameViewRect.y - 50),
                      pygame.math.Vector2(4, 1),
                      ShootType.DOUBLE, 20))
            _enemyList.add(
                Enemy("data/spiked ship 3.png", 1, (_gameViewRect.width, _gameViewRect.y - 50),
                      pygame.math.Vector2(-4, 1),
                      ShootType.DOUBLE, 20))
            self.spawned = 1

        if self.passedSeconds == 30 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship2.png", 1, (0, _gameViewRect.y - 50),
                      pygame.math.Vector2(3, 1),
                      ShootType.AIMED, 20))
            self.spawned = 1

        if self.passedSeconds == 32 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship2.png", 1, (0, _gameViewRect.y - 50),
                      pygame.math.Vector2(3, 1),
                      ShootType.AIMED, 20))
            self.spawned = 1

        if self.passedSeconds == 34 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship2.png", 1, (0, _gameViewRect.y - 50),
                      pygame.math.Vector2(3, 1),
                      ShootType.AIMED, 20))
            self.spawned = 1

        if self.passedSeconds == 36 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship2.png", 1, (0, _gameViewRect.y - 50),
                      pygame.math.Vector2(3, 1),
                      ShootType.AIMED, 20))
            self.spawned = 1

        if self.passedSeconds == 38 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship2.png", 1, (0, _gameViewRect.y - 50),
                      pygame.math.Vector2(3, 1),
                      ShootType.AIMED, 20))
            self.spawned = 1

        if self.passedSeconds == 45 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship5.png", 1, (_gameViewRect.x + _gameViewRect.width / 4, _gameViewRect.y - 50),
                      pygame.math.Vector2(0, 1),
                      ShootType.FOURDIRECTION, 20))

            _enemyList.add(
                Enemy("data/ship5.png", 1, (_gameViewRect.x + _gameViewRect.width * 3 / 4, _gameViewRect.y - 50),
                      pygame.math.Vector2(0, 2),
                      ShootType.FOURDIRECTION, 20))
            self.spawned = 1

        if self.passedSeconds == 50 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship1.png", 1, (_gameViewRect.width, _gameViewRect.y - 50),
                      pygame.math.Vector2(-2, 1),
                      ShootType.EIGHTDIRECTION, 20))
            self.spawned = 1

        if self.passedSeconds == 50 and self.spawned == 0:
            _enemyList.add(
                Enemy("data/ship1.png", 1, (_gameViewRect.width, _gameViewRect.y - 50),
                      pygame.math.Vector2(-2, 1),
                      ShootType.EIGHTDIRECTION, 20))
            self.spawned = 1
