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

# PHYSICS VARIABLES
gravity = 0
player_vel = 5
bullet_vel = 8

def draw_window(player, enemy, player_health):
    screen.fill(BACKGROUND_COLOUR)
    health_text = health_font.render("Health: " + str(player_health), 1, BLACK)
    screen.blit(health_text, (10, 10))
    

class Player(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets', 'sunwarriour.png'))
        self.damage = 1
        self.alive == True
        self.x = # in progress
        self.y = # in progress

    def image_load():
        pass

    def damage_output(self, alive, Enemy, damage):
        if alive == True:
            if # player hits enemy:
                # enemy health -= damage

    def movement(self, x, y, alive):
        keys_pressed = pygame.key.get_pressed()
        if alive == True:
            # Imports gravity and creates exponential relationship where gravity
            # increases exponentially and affects player's y position
            global gravity
            gravity += 0.8
            y += gravity

            # If player presses left arrow key they move left
            # and right arrow key moves right by certain amount
            if keys_pressed[pygame.K_LEFT]:
                x -= player_vel
            if keys_pressed[pygame.K_RIGHT]:
                x += player_vel

    def health_management(self, health, alive, kill_player):
        if alive == True:
            if health <= 0:
                kill_player()

    def kill_player(self, alive):
        if alive != True:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets', 'enemy.png'))
        self.damage = 5
        self.alive == True
        self.x = # in progress
        self.y = # in progress

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
            if # player hits enemy:
                kill_enemy()
    
    def kill_enemy(self, alive):
        if alive != True:
            self.kill()


class Boss(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets', 'boss.png'))
        self.damage = 10
        self.health = 10
        self.alive == True
        self.x = # in progress
        self.y = # in progress

    def image_load():
        pass

    def damage_output(self, x, damage, alive, player):
        if alive == True:
            if x - 5 <= player.x:
                player.health -= damage

    def movement(self, x, alive):
        if alive == True:
            x -= 2

    def health_management(self, health, alive, kill_boss):
        if alive == True:
            if # player hits boss:
                health -= 1
                if health <= 0:
                    kill_boss()

    def kill_boss(self, alive):
        if alive != True:
            self.kill()
            

def spawn_lose_text(lose_text):
    draw_lose_text = winner_font.render(lose_text, 1, BLACK)
    screen.blit(draw_lose_text, (WIDTH/2 - draw_lose_text.get_width()/2, HEIGHT/2 - draw_lose_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
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

    main()


if __name__ == "__main__":
    main()