import pygame
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 1500, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("Redmist.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
STAR_VEL = 3
STAR_WIDTH = 60
STAR_HEIGHT = 40

PLAYER_IMG = pygame.image.load("galaga.PNG").convert_alpha()
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))

STAR_IMG = pygame.image.load("Astroid.PNG").convert_alpha()
STAR_IMG = pygame.transform.scale(STAR_IMG, (STAR_WIDTH, STAR_HEIGHT))

pygame.mixer.init()
HIT_SOUND = pygame.mixer.Sound("explosion.wav")

FONT_SIZE = min(WIDTH, HEIGHT // 10)
FONT = pygame.font.SysFont("Montserrat", FONT_SIZE)


def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    for star in stars:
        rotated_star = pygame.transform.rotate(star["image"], star["angle"])
        rotated_rect = rotated_star.get_rect(center=star["rect"].center)
        WIN.blit(rotated_star, rotated_rect.topleft)

    WIN.blit(PLAYER_IMG, player.topleft)

    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star_angle = random.randint(0, 360)
                star_rect = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                star = {"rect": star_rect, "angle": star_angle, "image": STAR_IMG.copy()}
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star["rect"].y += STAR_VEL
            if star["rect"].y > HEIGHT:
                stars.remove(star)
            elif star["rect"].y + STAR_HEIGHT >= player.y and star["rect"].colliderect(player):
                stars.remove(star)
                HIT_SOUND.play()
                run = False
                break

        if run:  # Check if the game is still running before displaying the "YOU SUCK" text
            for star in stars:
                star["angle"] += 1  # Increment rotation angle for animation

            draw(player, elapsed_time, stars)

    if not run:  # Display "YOU SUCK" text after the game loop
        lost_text = FONT.render("YOU SUCK.", 1, "white")
        WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(4000)

    pygame.quit()


if __name__ == "__main__":
    main()


