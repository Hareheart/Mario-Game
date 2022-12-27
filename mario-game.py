import pygame
import os
pygame.font.init()


# WINDOW VARIABLES
WIDTH, HEIGHT = 1100, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Game")
FPS = 60

BACKGROUND_COLOR = "#230c06"
FIRST_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'secondmap.png')), (WIDTH, HEIGHT))
FINAL_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'firstmap.png')), (WIDTH, HEIGHT))

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

enemy_image = pygame.image.load(os.path.join('Assets', 'enemy.png'))
enemy_width = 60
enemy_height = 100

bullet_image = pygame.image.load(os.path.join('Assets', 'Bullet.png'))
bullet_width = 25
bullet_height = 10
bullet = pygame.transform.scale(bullet_image, (bullet_width, bullet_height))

# PHYSICS VARIABLES
gravity = 0
player_vel = 5
bullet_vel = 8
max_bullets = 3

def draw_window(player, enemy, bullets, player_health):
    screen.fill(BACKGROUND_COLOR)
    screen.blit(FIRST_BACKGROUND, (0, 0))

    health_text = health_font.render("Health: " + str(player_health), 1, BLACK)
    screen.blit(health_text, (10, 10))

    screen.blit(warrior_image, (player.x, player.y))
    screen.blit(enemy_image, (enemy.x, enemy.y))
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    pygame.display.update()


def physics(keys_pressed, player):
    global gravity
    gravity += 0.8
    player.y += gravity

    if keys_pressed[pygame.K_LEFT]:
        player.x -= player_vel
    if keys_pressed[pygame.K_RIGHT]:
        player.x += player_vel


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
    pygame.time.delay(3000)


def main():
    player = pygame.Rect(100, 100, warrior_width, warrior_height)
    enemy = pygame.Rect(700, 100, enemy_width, enemy_height)

    bullets = []

    player_health = 5

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # Jumping
                if event.key == pygame.K_UP:
                    global gravity
                    gravity = -10
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
        draw_window(player, enemy, bullets, player_health)

    main()


if __name__ == "__main__":
    main()