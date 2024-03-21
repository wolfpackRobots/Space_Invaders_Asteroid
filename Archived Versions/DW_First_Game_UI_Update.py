"""import pygame
import time
import random

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

# Load player image
PLAYER_IMG = pygame.image.load("galaga.PNG").convert_alpha()
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Load asteroid image
STAR_IMG = pygame.image.load("Astroid.PNG").convert_alpha()
STAR_IMG = pygame.transform.scale(STAR_IMG, (STAR_WIDTH, STAR_HEIGHT))

# Initialize sound effects
pygame.mixer.init()
HIT_SOUND = pygame.mixer.Sound("explosion.wav")

# Initialize font
FONT_SIZE = min(WIDTH, HEIGHT // 10)
FONT = pygame.font.SysFont("Montserrat", FONT_SIZE)


# Function to draw objects on the game window
def draw(player, elapsed_time, stars):
    global bg_y
    WIN.blit(BG, (0, bg_y))
    WIN.blit(BG, (0, bg_y - HEIGHT))

    # Render and display elapsed time
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Draw stars (asteroids)
    for star in stars:
        rotated_star = pygame.transform.rotate(star["image"], star["angle"])
        rotated_rect = rotated_star.get_rect(center=star["rect"].center)
        WIN.blit(rotated_star, rotated_rect.topleft)

    # Draw player
    WIN.blit(PLAYER_IMG, player.topleft)

    # Update display
    pygame.display.update()


# Function to display death message
def show_death_message():
    message = FONT.render("You died!", True, (255, 0, 0))
    WIN.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.update()
    time.sleep(2)  # Show the message for 2 seconds


# Main game loop
def main():
    global bg_y
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []  # Array to store information about stars (asteroids)

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        # Add stars (asteroids) to the game window
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star_angle = random.randint(0, 360)
                star_rect = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                star_vel = random.randint(1, 5)  # Generate a random velocity for the star
                star = {"rect": star_rect, "angle": star_angle, "image": STAR_IMG.copy(), "vel": star_vel}
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Set run to False to exit the main loop

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        # Update positions of stars (asteroids)
        for star in stars[:]:
            star["rect"].y += star["vel"]  # Move the star according to its velocity
            if star["rect"].y > HEIGHT:
                stars.remove(star)
            elif star["rect"].y + STAR_HEIGHT >= player.y and star["rect"].colliderect(player):
                stars.remove(star)
                HIT_SOUND.play()
                show_death_message()  # Shows the player death message
                run = False  # Set run to False to exit the main loop
                break  # Exit the collision detection loop

        # Rotate stars (asteroids) for animation
        for star in stars:
            star["angle"] += 1

        # Update background y position for scrolling effect
        bg_y = (bg_y + 1) % HEIGHT

        # Draw objects on the game window
        draw(player, elapsed_time, stars)

        # Check if the player is still alive
        if not run:
            time.sleep(2)  # Delay for 2 seconds after the player dies before quitting
            break

    pygame.quit()  # Make sure that pygame is properly closed after the main loop exits


# Start the game
if __name__ == "__main__":
    main()"""

import pygame
import time
import random

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

# Load player image
PLAYER_IMG = pygame.image.load("galaga.PNG").convert_alpha()
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Load asteroid image
STAR_IMG = pygame.image.load("Astroid.PNG").convert_alpha()
STAR_IMG = pygame.transform.scale(STAR_IMG, (STAR_WIDTH, STAR_HEIGHT))

# Initialize sound effects
pygame.mixer.init()
HIT_SOUND = pygame.mixer.Sound("explosion.wav")

# Initialize font
FONT_SIZE = min(WIDTH, HEIGHT // 10)
FONT = pygame.font.SysFont("Montserrat", FONT_SIZE)


# Function to draw objects on the game window
def draw(player, elapsed_time, stars):
    global bg_y
    WIN.blit(BG, (0, bg_y))
    WIN.blit(BG, (0, bg_y - HEIGHT))

    # Render and display elapsed time
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Draw stars (asteroids)
    for star in stars:
        rotated_star = pygame.transform.rotate(star["image"], star["angle"])
        rotated_rect = rotated_star.get_rect(center=star["rect"].center)
        WIN.blit(rotated_star, rotated_rect.topleft)

    # Draw player
    WIN.blit(PLAYER_IMG, player.topleft)

    # Update display
    pygame.display.update()


# Function to display death message
def show_death_message():
    message = FONT.render("You died!", True, (255, 0, 0))
    WIN.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.update()
    time.sleep(2)  # Show the message for 2 seconds


# Main game loop
def main():
    global bg_y
    run = True
    paused = False  # Initialize pause state

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []  # Array to store information about stars (asteroids)

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        # Add stars (asteroids) to the game window
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star_angle = random.randint(0, 360)
                star_rect = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                star_vel = random.randint(1, 5)  # Generate a random velocity for the star
                star = {"rect": star_rect, "angle": star_angle, "image": STAR_IMG.copy(), "vel": star_vel}
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Set run to False to exit the main loop
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = not paused  # Toggle pause state when 'p' is pressed

        # Check if the game is paused
        if paused:
            pause_text = FONT.render("PAUSE", True, (255, 255, 255))
            WIN.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - pause_text.get_height() // 2))
            pygame.time.delay(100) # Add a small delay to avoid high CPU usage during pause
            continue  # Skip the rest of the loop while paused

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        # Update positions of stars (asteroids)
        for star in stars[:]:
            star["rect"].y += star["vel"]  # Move the star according to its velocity
            if star["rect"].y > HEIGHT:
                stars.remove(star)
            elif star["rect"].y + STAR_HEIGHT >= player.y and star["rect"].colliderect(player):
                stars.remove(star)
                HIT_SOUND.play()
                show_death_message()  # Shows the player death message
                run = False  # Set run to False to exit the main loop
                break  # Exit the collision detection loop

        # Rotate stars (asteroids) for animation
        for star in stars:
            star["angle"] += 1

        # Update background y position for scrolling effect
        bg_y = (bg_y + 1) % HEIGHT

        # Draw objects on the game window
        draw(player, elapsed_time, stars)

        # Check if the player is still alive
        if not run:
            time.sleep(2)  # Delay for 2 seconds after the player dies before quitting
            break

    pygame.quit()  # Make sure that pygame is properly closed after the main loop exits


# Start the game
if __name__ == "__main__":
    main()
