import pygame
import time
import random
import pygame.sprite
from pygame.locals import KEYDOWN, KEYUP

# Initialize pygame
pygame.font.init()

# Set the dimensions of the game window
WIDTH, HEIGHT = 1500, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Load the background image
BG = pygame.transform.scale(pygame.image.load("Space.png"), (WIDTH, HEIGHT))
bg_y = 0

# Player constants
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

# Asteroid constants
STAR_WIDTH = 60
STAR_HEIGHT = 40

# Projectile constants
PROJECTILE_WIDTH = 5
PROJECTILE_HEIGHT = 15
PROJECTILE_VEL = 10
PROJECTILE_COLOR = (255, 0, 0)

# Load player image
PLAYER_IMG = pygame.image.load("galaga.png").convert_alpha()
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Load asteroid image
STAR_IMG = pygame.image.load("Asteroid.png").convert_alpha()
STAR_IMG = pygame.transform.scale(STAR_IMG, (STAR_WIDTH, STAR_HEIGHT))

# Initialize sound effects
pygame.mixer.init()
HIT_SOUND = pygame.mixer.Sound("explosion.wav")
SHOOT_SOUND = pygame.mixer.Sound("shoot.wav")

# Initialize font
FONT_SIZE = min(WIDTH, HEIGHT // 10)
FONT = pygame.font.SysFont("Montserrat", FONT_SIZE)

# Explosion class definition
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.size = size
        self.images = []
        for i in range(1, 5):
            image = pygame.image.load(f"exp{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (size * 20, size * 20))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0

    def update(self):
        explosion_speed = 3
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        elif self.index >= len(self.images) - 1:
            self.kill()

# Function to draw objects on the game window
def draw(player, projectiles, elapsed_time, stars, all_sprites, score):
    global bg_y
    WIN.blit(BG, (0, bg_y))
    WIN.blit(BG, (0, bg_y - HEIGHT))

    # Render and display elapsed time
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Render and display score directly below elapsed time
    score_text = FONT.render(f"Score: {score}", 1, "white")
    WIN.blit(score_text, (10, 70))  # Adjusted y-coordinate to move score area downwards

    # Draw stars (asteroids)
    for star in stars:
        rotated_star = pygame.transform.rotate(star["image"], star["angle"])
        rotated_rect = rotated_star.get_rect(center=star["rect"].center)
        WIN.blit(rotated_star, rotated_rect.topleft)

    # Draw player
    WIN.blit(PLAYER_IMG, player.topleft)

    # Draw projectiles
    for projectile in projectiles:
        pygame.draw.rect(WIN, PROJECTILE_COLOR, projectile)

    # Draw explosions
    all_sprites.draw(WIN)

    # Update display
    pygame.display.update()

# Function to display death message and prompt to play again
def show_death_message():
    message = FONT.render("You died! Would you like to play again? (Y/N)", True, (255, 0, 0))
    WIN.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True  # Player wants to play again
                elif event.key == pygame.K_n:
                    return False  # Player doesn't want to play again

# Main game loop
def main():
    global bg_y
    
    while True:  # Loop to handle replay
        run = True
        paused = False
        player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
        player_alive = True  # Flag to track player's life

        clock = pygame.time.Clock()
        start_time = time.time()
        elapsed_time = 0
        star_add_increment = 2000
        star_count = 0
        stars = []  
        projectiles = []  
        space_pressed = False  
        shoot_delay = 0.2  
        last_shot_time = 0  

        all_sprites = pygame.sprite.Group()  # Create a sprite group for explosions

        score = 0  # Initialize score

        while run:
            star_count += clock.tick(60)
            elapsed_time = time.time() - start_time

            if star_count > star_add_increment:
                for _ in range(3):
                    star_x = random.randint(0, WIDTH - STAR_WIDTH)
                    star_angle = random.randint(0, 360)
                    star_rect = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                    star_vel = random.randint(1, 5) 
                    star = {"rect": star_rect, "angle": star_angle, "image": STAR_IMG.copy(), "vel": star_vel}
                    stars.append(star)
                star_add_increment = max(200, star_add_increment - 50)
                star_count = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False  # Set run to False to exit the main loop
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = not paused  # Toggle pause state when 'ESCAPE' is pressed
                    elif event.key == pygame.K_SPACE:
                        space_pressed = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        space_pressed = False

            # Check if the game is paused
            if paused:
                pause_text = FONT.render("PAUSE", True, (255, 255, 255))
                WIN.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - pause_text.get_height() // 2))
                pygame.time.delay(100) # Add a small delay to avoid high CPU usage during pause
                continue  # Skip the rest of the loop while paused

            current_time = time.time()
            if space_pressed and current_time - last_shot_time > shoot_delay:
                projectile = pygame.Rect(player.centerx - PROJECTILE_WIDTH // 2, player.y, PROJECTILE_WIDTH, PROJECTILE_HEIGHT)
                projectiles.append(projectile)
                SHOOT_SOUND.play()  
                last_shot_time = current_time

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL
            if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
                player.y -= PLAYER_VEL
            if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
                player.y += PLAYER_VEL

            if player_alive:  # Only update game logic if the player is alive
                for star in stars[:]:
                    star["rect"].y += star["vel"]
                    if star["rect"].y > HEIGHT:
                        stars.remove(star)
                    elif star["rect"].colliderect(player):
                        stars.remove(star)
                        HIT_SOUND.play()
                        player_alive = False
                        break
                for projectile in projectiles[:]:
                    projectile.y -= PROJECTILE_VEL
                    if projectile.y + PROJECTILE_HEIGHT < 0:
                        projectiles.remove(projectile)
                    else:
                        for star in stars[:]:
                            if star["rect"].colliderect(projectile):
                                # Create an explosion at the asteroid's position
                                explosion = Explosion(star["rect"].centerx, star["rect"].centery, size=2)
                                # Add the explosion to a sprite group for updating and rendering
                                all_sprites.add(explosion)
                                # Remove the asteroid and projectile
                                stars.remove(star)
                                projectiles.remove(projectile)
                                HIT_SOUND.play()
                                # Increase the score when an asteroid is destroyed
                                score += 1
                                break  
                        else:  # This else clause is executed if no collision occurred
                            continue  # Skip the rest of the loop
                        break  # Break the loop if collision occurred

                for star in stars:
                    star["angle"] += 1

            bg_y = (bg_y + 1) % HEIGHT

            draw(player, projectiles, elapsed_time, stars, all_sprites, score)

            # Update explosion animations
            all_sprites.update()

            if not player_alive:  # If player is dead, show death message and exit after a delay
                if not show_death_message():  # If player doesn't want to play again
                    run = False
                    break  # Exit game loop
                else:  # Player wants to play again
                    break  # Exit inner loop to restart the game

        if not run:  # If player doesn't want to play again, exit outer loop
            break

    pygame.quit()

if __name__ == "__main__":
    main()