import pygame
import os
pygame.font.init()


# WINDOW VARIABLES
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Game")

WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0

FPS = 60

health_font = pygame.font.SysFont('comicsans', 40)
winner_font = pygame.font.SysFont('comicsans', 100)

# EVENTS
player_hit = pygame.USEREVENT + 1

# SPRITE VARIABLES
block_image = pygame.image.load(os.path.join('block.png'))
block_width = 60
block_height = 60
block = pygame.transform.scale(block_image, (block_width, block_height))

ground_width = WIDTH
ground_height = 10
ground = pygame.Rect(0, (HEIGHT/2) - (ground_height/2), WIDTH, ground_height)

bullet_width = 25
bullet_height = 10

# PHYSICS VARIABLES
gravity = 5
vel_x = 5
vel_y = 100
bullet_vel = 8
max_bullets = 3


def draw_window(player, bullets, player_health):
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, ground)

    health_text = health_font.render("Health: " + str(player_health), 1, BLACK)
    screen.blit(health_text, (10, 10))

    screen.blit(block, (player.x, player.y))
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    pygame.display.update()


def physics(keys_pressed, player):
    if player.y < (HEIGHT/2) - block_height:
        player.y += gravity
    if keys_pressed[pygame.K_LEFT]:
        player.x -= vel_x
    if keys_pressed[pygame.K_RIGHT]:
        player.x += vel_x

def move_bullets(bullets, player):
    for bullet in bullets:
        bullet.x += bullet_vel
        if player.colliderect(bullet):
            pygame.event.post(pygame.event.Event(player_hit))
            bullets.remove(bullet)
        if bullet.x > WIDTH:
            bullets.remove(bullet)

    
def spawn_lose_text(lose_text):
    draw_lose_text = winner_font.render(lose_text, 1, BLACK)
    screen.blit(draw_lose_text, (WIDTH/2 - draw_lose_text.get_width()/2, HEIGHT/2 - draw_lose_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    player = pygame.Rect(100, 100, block_width, block_height)

    bullets = []

    player_health = 5

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                # Jumping
                if event.key == pygame.K_UP:
                    player.y -= vel_y
                # Shooting
                if event.key == pygame.K_SPACE and len(bullets) < max_bullets:
                    bullet = pygame.Rect(
                        player.x + player.width, player.y + (player.height/2), bullet_width, bullet_height)
                    bullets.append(bullet)

            if event.type == player_hit:
                player_health -= 1
        
        lose_text = ""
        if player_health <= 0:
            lose_text = "You lose!"

        if lose_text != "":
            spawn_lose_text(lose_text)
            break

        keys_pressed = pygame.key.get_pressed()
        physics(keys_pressed, player)
        move_bullets(bullets, player)
        draw_window(player, bullets, player_health)

    pygame.quit()


if __name__ == "__main__":
    main()