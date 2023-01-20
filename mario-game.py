import pygame, os
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
        mdata.run()
        pygame.display.update()


if __name__ == "__main__":
    main()