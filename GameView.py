import pygame
from View import View
from Enemy import Enemy, ShootType
from Level1 import Level1

class GameView(View):

    enemyList = pygame.sprite.Group()
    bulletList = pygame.sprite.Group()
    playerBulletList = pygame.sprite.Group()

    def __init__(self, _surface, _rekt, _player, _engine):
        super(GameView, self).__init__(_surface, _rekt, _player, _engine)

    def newGame(self):
        self.activeLevel = Level1()
        self.enemyList.empty()
        self.bulletList.empty()
        self.playerBulletList.empty()

    def onEvent(self, _event):

        if _event.type == pygame.KEYDOWN:
            if _event.key == pygame.K_z:
                self.playerBulletList.add(self.player.shoot())

    def render(self):

        self.player.render(self.surface)
        for bullet in self.bulletList:
            bullet.render(self.surface)

        for playerBullet in self.playerBulletList:
            playerBullet.render(self.surface)

        for enemy in self.enemyList:
            enemy.render(self.surface)

        super(GameView, self).render()

    def onTick(self, _clock):

        # aktualizowanie stanu aktualnego poziomu, czyli tworzenie wrogich statkow
        self.activeLevel.update(_clock, self.enemyList, self.rect, self, self.player, self.ref_engine)

        # ruch gracza
        key = pygame.key.get_pressed()

        right = key[pygame.K_RIGHT]
        left = key[pygame.K_LEFT]
        up = key[pygame.K_UP]
        down = key[pygame.K_DOWN]

        self.player.move(self, pygame.math.Vector2(right - left, down - up))

        #poruszanie sie strzalow przeciwnikow
        for bullet in self.bulletList:
            if bullet.move(self):
                self.bulletList.remove(bullet)

        # poruszanie sie strzalow gracza
        for playerBullet in self.playerBulletList:
            if playerBullet.move(self):
                self.playerBulletList.remove(playerBullet)

        # poruszanie sie przeciwnikow
        for enemy in self.enemyList:
            if enemy.move(self):
                self.enemyList.remove(enemy)

        # strzelanie przeciwnikow
        for enemy in self.enemyList:
            enemy.shoot(self.bulletList, self.player.rect)

        #kolizje

        lista = pygame.sprite.spritecollide(self.player, self.bulletList, 1)
        lista2 = pygame.sprite.spritecollide(self.player, self.enemyList, 1)
        lista3 = pygame.sprite.groupcollide(self.enemyList, self.playerBulletList, 1, 1)

        for bullet in lista:
            self.player.multp = 1
            self.player.lives -= 1
            if self.player.lives == 0:
                self.ref_engine.lastScore = self.player.score
                self.ref_engine.setActiveScreen('Gameover')

        for enemy in lista2:
            self.player.multp = 1
            self.player.lives -= 1
            if self.player.lives == 0:
                self.ref_engine.lastScore = self.player.score
                self.ref_engine.setActiveScreen('Gameover')

        for enemy in lista3:
            self.player.multp += 1
            if enemy.shootType == ShootType.AIMED:
                self.player.score += self.player.multp * 200
            elif enemy.shootType == ShootType.EIGHTDIRECTION:
                self.player.score += self.player.multp * 500
            elif enemy.shootType == ShootType.FOURDIRECTION:
                self.player.score += self.player.multp * 400
            elif enemy.shootType == ShootType.DOUBLE:
                self.player.score += self.player.multp * 100
            elif enemy.shootType == ShootType.NORMAL:
                self.player.score += self.player.multp * 50

        # usuwanie przeciwnikow poza ekranem
        for enemy in self.enemyList:
            if enemy.rect.y > self.ref_engine.screen.get_height() + enemy.rect.height:
                self.enemyList.remove(enemy)

