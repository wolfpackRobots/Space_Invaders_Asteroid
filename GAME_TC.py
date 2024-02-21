#It is mandatory to sing on three different occasions in a King's Quest 7 speedrun in order for it to be accepted. One is about the creator of the series drinking Franzia on her yacht and pissing on herself, which is sung twice. The other song is the song that plays in the end credits. Again, these are mandatory, at least for runs on world record pace. The average time of all runs with the Franzia song is 50:03. The average length of all runs without singing a song that is as pleasing as the RE basement theme is 53:36. Therefore, singing about Roberta Williams pissing herself after drinking multiple boxes of box wine is DEFINITELY a speedrun strategy with no flaws. 

#How to make a game in python by tech with tim
import pygame #GUI
import time #allows counting, but why do we need this if pygame has a timer?
import random #adds random number generation, usually as a float value
pygame.font.init()

WIDTH, HEIGHT = 1500, 768
# this is window size
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # why double parentheses
pygame.display.set_caption("Space Dodge") #name of the game

# BG = pygame.image.load("Utah_map.jpg")
BG = pygame.transform.scale(pygame.image.load("lastgen.jpeg"),(WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
STAR_VEL = 3
STAR_WIDTH = 10
STAR_HEIGHT = 20

PLAYER_IMG = pygame.image.load("Galaga.PNG").convert_alpha()
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))

FONT = pygame.font.SysFont("Montserrat", 30)


def draw(player, elapsed_time, stars):
    WIN.blit(BG,  (0,0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s" , 1, "white")
    WIN.blit(time_text, (10, 10)) #coords for text
    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    
    # pygame.draw.rect(WIN, (255, 0, 0)) #it's RGB, figure out the rest shitlips
    #pygame.transform.scale(pygame.image.load("yuda.jpeg"),(PLAYER_WIDTH, PLAYER_HEIGHT))(WIN, player) #error likely not due to having pygame installed
    WIN.blit(PLAYER_IMG, player.topleft)
    
    pygame.display.update()

def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()
    
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 2000 #time between adding stars
    star_count = 0 #starts generation of stars
    
    stars = []
    hit = []
    
    while run:
        star_count += clock.tick(60) #restricts how often this runs
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            for _ in range(3): #why is underscore here
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT) #NEGATIVE STAR HEIGHT because moving down
                stars.append(star)
            star_add_increment = max(200, star_add_increment-50) #why minus 50
            star_count = 0
            
            
        #clock.tick(60)
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
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
                
        if hit:
            lost_text = FONT.render ("YOU HAVE DIED.", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
                
        draw(player, elapsed_time, stars)
    pygame.quit()
    
if __name__ == "__main__":
    main()