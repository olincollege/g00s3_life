"""
main game docstring

"""
# Import the pygame module
import pygame
from constraints import SCREEN_WIDTH
from constraints import SCREEN_HEIGHT
from character import Player
from character import Enemy
from character import Cloud
from character import Coin

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    #RLEACCEL,
    #K_UP,
    #K_DOWN,
    #K_LEFT,
    #K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
sky_bg = pygame.image.load('images/Goose_Life_Skybox.png')
sky_bg = pygame.transform.scale(sky_bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
sky_bg = pygame.transform.rotate(sky_bg,180)
hills_bg = pygame.image.load('images/Goose_Life_Rolling_Background_2.png')
hills_bg = pygame.transform.scale(hills_bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
transColor = hills_bg.get_at((0,0))
hills_bg.set_colorkey(transColor)

i = 0
# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1500)
ADDCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCOIN, round(1500/5))


clock = pygame.time.Clock()
# Instantiate player. Right now, this is just a rectangle.
player = Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Variable to keep the main loop running
running = True
score = 0


# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

        elif event.type == ADDCOIN:
            # Create the new enemy and add it to sprite groups
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        
    for coin in coins:
        if player.rect.colliderect(coin):
            coin.kill()
            score+=1
    

    if pygame.sprite.spritecollideany(player, enemies):
    # If so, then remove the player and stop the loop
        player.kill()
        running = False

    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()
    clouds.update()
    
    #update coins
    coins.update()

    # Draw the sky background
    screen.blit(sky_bg,(0,0))

    #Draw the hills
    screen.blit(hills_bg,(i,0))
    screen.blit(hills_bg,(SCREEN_WIDTH+i,0))
    if (i==-SCREEN_WIDTH):
        screen.blit(hills_bg,(SCREEN_WIDTH+i,0))
        i=0
    i -= 1

    # Draw the player on the screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, (255, 255, 255))
    screen.blit(text, (250,10))


    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(60)
