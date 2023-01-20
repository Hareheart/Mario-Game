import pygame, os, sys
from maps import mapdata1
from layerinfo import level_1


pygame.font.init()
pygame.init()
pygame.display.init()

# WINDOW VARIABLES
WIDTH, HEIGHT = 480, 352
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ghoul Harvester")
FPS = 60
mdata = mapdata1(level_1, screen)

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

            if event.type == player_hit:
                player_health -= 1
        mdata.run()
        pygame.display.update()


if __name__ == "__main__":
    main()