"""
stores functions and classes we call in order to play the game

"""
# importing needed libraries
import pygame
import pygame.freetype
import sys
from constraints import SCREEN_WIDTH
from constraints import SCREEN_HEIGHT
from character import Player
from character import RainbowPlayer
from character import Enemy
from character import Cloud
from character import BigCloud
from character import Coin

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    # RLEACCEL,
    # K_UP,
    # K_DOWN,
    # K_LEFT,
    # K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

# Defining variables
global score

# Setting up screens
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#Game window
start_screen = pygame.image.load('images/titlescreen.PNG')#Start Screen
loss_screen = pygame.image.load('images/newoof.PNG')#End Screen

# Formatting background images
sky_bg = pygame.image.load('images/Goose_Life_Skybox.png')
sky_bg = pygame.transform.scale(sky_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
sky_bg = pygame.transform.rotate(sky_bg, 180)
hills_bg = pygame.image.load('images/Goose_Life_Rolling_Background_2.png')
hills_bg = pygame.transform.scale(hills_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
bad_color = hills_bg.get_at((0, 0))
hills_bg.set_colorkey(bad_color)

# Setting up in-game clock for frame-rate purposes
clock = pygame.time.Clock()
running = True
score = 0

# Setting up in-game sprite groups 
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
big_clouds = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Setting up in-game events and how often they occur
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1500)
ADDCOIN = pygame.USEREVENT + 3
pygame.time.set_timer(ADDCOIN, round(300))
ADDBIGCLOUD = pygame.USEREVENT + 4
pygame.time.set_timer(ADDCLOUD, 2000)

# Starts pygame
pygame.init()

def play_level(screen):
    """
    Play the game

    Args:
        screen: The screen on which the game is displayed

    Returns:
        score: The number of coins that the player collected in their runtime
    """
    #Initializes the game states
    global score, running
    score = 0
    i = 0
    player = Player()
    all_sprites.add(player)
    rainbow = False # Has the condition for rainbow bird been achieved?

    #Runs the actual game
    while running:
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

            # Add a new coin
            elif event.type == ADDCOIN:
                # Create the new coin and add it to sprite groups
                new_coin = Coin()
                coins.add(new_coin)
                all_sprites.add(new_coin)

            # Add a new big cloud
            elif event.type == ADDBIGCLOUD:
                # Create the new big cloud and add it to sprite groups
                new_big_cloud = BigCloud()
                big_clouds.add(new_big_cloud)
                all_sprites.add(new_big_cloud)

        # Are we supposed to be rainbow?
        if score > 14:
            # Have we already changed the goose?
            if rainbow is False:
                # Replace the current player, in the same position, with the
                # rainbow goose
                current_x = player.rect.x
                current_y = player.rect.y
                player.kill()
                new_player = RainbowPlayer(current_x, current_y)
                all_sprites.add(new_player)
                rainbow = True
            # Move the rainbow goose
            update_player(new_player)

        else:
            #Move the regular goose
            update_player(player)

        # Update sprite positions
        enemies.update()
        clouds.update()
        coins.update()
        big_clouds.update()

        # Draw the sky background
        screen.blit(sky_bg, (0, 0))

        # Draw the hills and their movement
        screen.blit(hills_bg, (i, 0))
        screen.blit(hills_bg, (SCREEN_WIDTH+i, 0))
        if i == -SCREEN_WIDTH:
            screen.blit(hills_bg, (SCREEN_WIDTH+i, 0))
            i = 0
        i -= 1

        # Draw all entities on the screen
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        #Display the score
        font = pygame.font.Font(None, 74)
        text = font.render(str(score), 1, (255, 255, 255))
        screen.blit(text, (10, SCREEN_HEIGHT-50))

        # Update the display
        pygame.display.flip()

        # Ensure program maintains a rate of 60 frames per second
        clock.tick(60)

        if running is False:
            return score

def update_player(goose):
    """
    Runs all the processes that are related to the player being controlled

    Args:
        version: Establishes if the goose is rainbow or not
    """
    # Globals
    global score, running

    # Find which key, if any, is being pressed
    pressed_keys = pygame.key.get_pressed()

    # If the goose collides, go to end screen
    if pygame.sprite.spritecollideany(goose, enemies):
        for entity in all_sprites:
            entity.kill()
        running = False

    # Moves the goose
    goose.update(pressed_keys)

    # Collects coins and updates score
    for coin in coins:
        if goose.rect.colliderect(coin):
            coin.kill()
            score += 1

    

def check_for_key_press():
    """
    Checks for if any key is pressed and then released

    Returns:
        The identity of the key that was pressed and then released (or None)
    """
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    key_up_events = pygame.event.get(KEYUP)
    if len(key_up_events) == 0:
        return None
    if key_up_events[0].key == K_ESCAPE:
        terminate()
    return key_up_events[0].key


def terminate():
    """
    Quits the game and closes the window
    """
    pygame.quit()
    sys.exit()


def title_screen(screen):
    """
    Displays the title screen

    Args:
        screen: the screen on which the game is drawn
    """
    #Displays art and text
    titleFont = pygame.font.Font(None, 40)
    pressKeySurf = titleFont.render('Press any key!', True, (0, 0, 0))
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.bottomright = (SCREEN_WIDTH-10, SCREEN_HEIGHT-5)
    screen.blit(start_screen, (0, 0)) # Art
    screen.blit(pressKeySurf, pressKeyRect) # Text

    #Initiates gameplay
    while True:
        if check_for_key_press():
            pygame.event.get()  # clear event queue
            return
        pygame.display.flip()


def end_screen(screen, score):
    """
    Displays the screen that appears when the player loses/is hit by an enemy

    Args:
        screen: The screen on which the game is displayed
        score: The amount of coins the player collected during this run
    """
    # Chooses which text, based on score, to display
    titleFont = pygame.font.Font(None, 40)
    if score < 15:
        pressKeySurf = titleFont.render(
            'But can you make it to 15? Try again!', True, (0, 0, 0))
    elif score < 50:
        pressKeySurf = titleFont.render(
            'But can you make it all the way to 50? Try again!', \
                True, (0, 0, 0))
    else:
        pressKeySurf = titleFont.render(':)', True, (0, 0, 0))
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.bottomright = (SCREEN_WIDTH-10, SCREEN_HEIGHT-5)

    # Displays art and text
    screen.blit(loss_screen, (0, 0)) # Art
    screen.blit(pressKeySurf, pressKeyRect) # Text

    # Makes sure nobody accidentally restarts before they see the screen
    pygame.display.update()
    pygame.time.wait(500)
    check_for_key_press()

    # Restarts gameplay
    global running
    while True:
        if check_for_key_press():
            pygame.event.get()
            running = True
            return

        pygame.display.flip()
