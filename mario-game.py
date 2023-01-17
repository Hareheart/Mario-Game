import pygame, os, sys
from maps import mapdata
from layerinfo import level_1


pygame.font.init()
pygame.init()
pygame.display.init()
# WINDOW VARIABLES
WIDTH, HEIGHT = 480, 352
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ghoul Harvester")
FPS = 60
mdata = mapdata(level_1, screen)

BACKGROUND_COLOUR = 79, 12, 6
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0

# FONTS
health_font = pygame.font.SysFont('comicsans', 40)
winner_font = pygame.font.SysFont('comicsans', 100)

# EVENTS
player_hit = pygame.USEREVENT + 1

# SPRITE VARIABLES
warrior_image = pygame.image.load(os.path.join('Assets', 'warrior.png'))
warrior_width = 60
warrior_height = 100

# PHYSICS VARIABLES
gravity = 0
player_vel = 5
bullet_vel = 8

def draw_window(player, enemy, player_health):
    screen.fill(BACKGROUND_COLOUR)
    health_text = health_font.render("Health: " + str(player_health), 1, BLACK)
    screen.blit(health_text, (10, 10))
    screen.blit(warrior_image, (player.x, player.y))
    

class Enemy(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets', 'enemy.png'))
        self.damage = 5
        self.alive == True
        # Blaze work
        self.x = 
        self.y = 

    def image_load(self, image, time):
        pass
        # enemy = pygame.Rect(700, 100, 60, 100)
        # screen.blit(enemy_image, (enemy.x, enemy.y))

    def damage_output(self, x, damage, alive, player):
        if alive == True:
            if x == player.x:
                player.health -= damage

    def movement(self, x, alive):
        if alive == True:
            # Blaze will work on this
            x -= 2

    def die(self, alive):
        if alive != True:
            self.kill()


class Boss(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets', 'boss.png'))
        self.damage = 10
        self.alive == True
        # Blaze work
        self.x = 
        self.y = 

    def image_load():
        pass

    def damage_output(self, x, damage, alive, player):
        if alive == True:
            if x - 5 <= player.x:
                player.health -= damage

    def movement(self, x, alive):
        if alive == True:
            x -= 2

    def die(self, alive):
        if alive != True:
            self.kill()


def physics(keys_pressed, player):
    global gravity
    gravity += 0.8
    player.y += gravity

    if keys_pressed[pygame.K_LEFT]:
        player.x -= player_vel
    if keys_pressed[pygame.K_RIGHT]:
        player.x += player_vel


def spawn_lose_text(lose_text):
    draw_lose_text = winner_font.render(lose_text, 1, BLACK)
    screen.blit(draw_lose_text, (WIDTH/2 - draw_lose_text.get_width()/2, HEIGHT/2 - draw_lose_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    player = pygame.Rect(100, 100, warrior_width, warrior_height)

    player_health = 5

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                # Jumping
                if event.key == pygame.K_UP:
                    global gravity
                    gravity = -10

            if event.type == player_hit:
                player_health -= 1
        mdata.run()
        pygame.display.update()
        lose_text = ""
        if player_health == 0:
            lose_text = "You lose!"

        if lose_text != "":
            spawn_lose_text(lose_text)
            break

        keys_pressed = pygame.key.get_pressed()
        physics(keys_pressed, player)
        draw_window(player, enemy, player_health)

    main()


if __name__ == "__main__":
    main()