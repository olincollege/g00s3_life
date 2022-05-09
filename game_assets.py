"""
stores functions and classes we call in order to play the game

"""
#importing needed libraries
import pygame
import pygame.freetype
import sys

# Import the pygame module
import pygame
from constraints import SCREEN_WIDTH
from constraints import SCREEN_HEIGHT
from character import Player
from character import RainbowPlayer
from character import Enemy
from character import Cloud
from character import BigCloud
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
    KEYUP,
    QUIT,
)

#defining variables
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
start_screen = pygame.image.load('images/titlescreen.PNG')
loss_screen = pygame.image.load('images/newoof.PNG')
sky_bg = pygame.image.load('images/Goose_Life_Skybox.png')
sky_bg = pygame.transform.scale(sky_bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
sky_bg = pygame.transform.rotate(sky_bg,180)
hills_bg = pygame.image.load('images/Goose_Life_Rolling_Background_2.png')
hills_bg = pygame.transform.scale(hills_bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
bad_color = hills_bg.get_at((0,0))
hills_bg.set_colorkey(bad_color)
clock = pygame.time.Clock()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
big_clouds = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1500)
ADDCOIN = pygame.USEREVENT + 3
pygame.time.set_timer(ADDCOIN, round(300))
ADDBIGCLOUD = pygame.USEREVENT + 4
pygame.time.set_timer(ADDCLOUD, 4000)
# Variable to keep the main loop running


#initializing pygame
pygame.init()


#first function
def play_level(screen):
    """

    Args:

    Returns: Runs the main game

    """
    i = 0
    score = 0
    player = Player()
    all_sprites.add(player)
    rainbow = False

    while True:
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then close the game.
                if event.key == K_ESCAPE:
                    terminate()
            # Check for QUIT event. If QUIT, then close the game.
            elif event.type == QUIT:
                terminate()
            # Add a new enemy
            elif event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            # Add a new cloud
            elif event.type == ADDCLOUD:
                # Create the new cloud and add it to sprite groups
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)
            elif event.type == ADDCOIN:
                # Create the new coin and add it to sprite groups
                new_coin = Coin()
                coins.add(new_coin)
                all_sprites.add(new_coin)
            elif event.type == ADDBIGCLOUD:
                # Create the new cloud and add it to sprite groups
                new_big_cloud = BigCloud()
                big_clouds.add(new_big_cloud)
                all_sprites.add(new_big_cloud)

        pressed_keys = pygame.key.get_pressed()

        if score > 19:
            if rainbow is False:
                current_x = player.rect.x
                current_y = player.rect.y
                player.kill()
                new_player = RainbowPlayer(current_x, current_y)
                all_sprites.add(new_player)
                rainbow = True

            if pygame.sprite.spritecollideany(new_player, enemies):
                for entity in all_sprites:
                    entity.kill()
                return score#exits game when player dead

            new_player.update(pressed_keys)

            for coin in coins:
                if new_player.rect.colliderect(coin):
                    coin.kill()
                    score+=1
        else:
            if pygame.sprite.spritecollideany(player, enemies):
                for entity in all_sprites:
                    entity.kill()
                return score#exits game when player dead
            player.update(pressed_keys)

            for coin in coins:
                if player.rect.colliderect(coin):
                    coin.kill()
                    score+=1
        # Update the player sprite based on user keypresses

        # Update sprite positions
        enemies.update()
        clouds.update()
        coins.update()
        big_clouds.update()

        # Draw the sky background
        screen.blit(sky_bg,(0,0))

        #Draw the hills
        screen.blit(hills_bg,(i,0))
        screen.blit(hills_bg,(SCREEN_WIDTH+i,0))
        if i==-SCREEN_WIDTH:
            screen.blit(hills_bg,(SCREEN_WIDTH+i,0))
            i=0
        i -= 1

        # Draw the player on the screen
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        font = pygame.font.Font(None, 74)
        text = font.render(str(score), 1, (255, 255, 255))
        screen.blit(text, (10,SCREEN_HEIGHT-80))


        # Update the display
        pygame.display.flip()

        # Ensure program maintains a rate of 60 frames per second
        clock.tick(60)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def terminate():
    pygame.quit()
    sys.exit()

def title_screen(screen):
    titleFont = pygame.font.Font(None, 40)
    pressKeySurf = titleFont.render('Press any key!', True, (0,0,0))
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.bottomright = (SCREEN_WIDTH-10, SCREEN_HEIGHT-5)

    while True:
        screen.blit(start_screen,(0,0))
        screen.blit(pressKeySurf, pressKeyRect)
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.flip()

def end_screen(screen, score):
    """
    """
    titleFont = pygame.font.Font(None, 40)
    if score < 20:
        pressKeySurf = titleFont.render('But can you make it to 20? Try again!', True, (0,0,0))
    else:
        pressKeySurf = titleFont.render('Good job! But can you get higher?', True, (0,0,0))
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.bottomright = (SCREEN_WIDTH-10, SCREEN_HEIGHT-5)

    screen.blit(loss_screen,(0,0))
    screen.blit(pressKeySurf, pressKeyRect)
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()

    while True:
        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.flip()