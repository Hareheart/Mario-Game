import pygame, os
from random import randint


class Player(pygame.sprite.Sprite):
    def _init_(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load(os.path.join('Assets', 'sunwarriour.png'))
        self.damage = 1
        self.alive == True
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 3
        self.gravity = 0
        self.hit = False

    def damage_output(self, hit):
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN:
            hit = True

    def movement(self, speed, pos, gravity):
        keys_pressed = pygame.key.get_pressed()

        # Gravity increases exponentially and pulls player down
        gravity += 0.8
        y += gravity

        if keys_pressed[pygame.K_LEFT]:
            pos.x -= speed
        if keys_pressed[pygame.K_RIGHT]:
            pos.x += speed
        
        # Gravity moves player in opposite direction and functions as jump
        if keys_pressed[pygame.K_SPACE]:
            gravity = -10

    def health_management(self, health, kill_player):
        if health <= 0:
            kill_player()

    def kill_player(self, alive):
        if alive != True:
            self.kill()

    def update(self):
        self.damage_output()
        self.movement()
        self.health_management()
            

class Enemy(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.speed = randint(2,5)
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)
    
    def move(self):
        self.rect.x += self.speed

    def reverse(self):
        self.speed *= -1

    def damage_output(self, x, damage, player):
        if x == player.x:
            player.health -= damage

    def health_management(self, kill_enemy):
        if :
            kill_enemy()
            

    def kill_enemy(self, alive):
        self.kill()

    def update(self,shift):
        self.rect.x += shift
        self.move()
        self.reverse_image()
        self.damage_output()
        self.health_management()