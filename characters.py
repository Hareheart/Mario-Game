import pygame, os
from random import randint


class Enemy(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets', 'enemy.png'))
        self.damage = 5
        self.alive == True
        #self.x =  in progress
        #self.y =  in progress

    def image_load(self, image, time):
        pass

    def damage_output(self, x, damage, alive, player):
        if alive == True:
            if x == player.x:
                player.health -= damage

    def movement(self, x, alive):
        if alive == True:
            # Blaze will work on this
            x -= 2

    def health_management(self, alive, kill_enemy):
        if alive == True:
            #if player hits enemy:
            #kill_enemy()
            pass

    def kill_enemy(self, alive):
        if alive != True:
            self.kill()
