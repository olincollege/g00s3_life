# Import the pygame module
import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 560

game_speed=5

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("goose.jpg").convert()
        self.surf = pygame.transform.scale(self.surf, (32, 48)) 
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.y = SCREEN_HEIGHT/2
        self.rect.x = 100

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()
        self.surf = pygame.Surface((15, 15))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = 10

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed*game_speed, 0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("Goose_Life_Cloud.png").convert()
        self.surf = pygame.transform.scale(self.surf, (60, 60)) 
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5*game_speed, 0)
        if self.rect.right < 0:
            self.kill()

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
sky_bg = pygame.image.load('Goose_Life_Skybox.png')
sky_bg = pygame.transform.scale(sky_bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
sky_bg = pygame.transform.rotate(sky_bg,180)
hills_bg = pygame.image.load('Goose_Life_Rolling_Background_2.png')
hills_bg = pygame.transform.scale(hills_bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
transColor = hills_bg.get_at((0,0))
hills_bg.set_colorkey(transColor)


i = 0
# Create a custom event for adding a new enemy
ADDCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCOIN, round(1500/game_speed))
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, round(2000/game_speed))

clock = pygame.time.Clock()
# Instantiate player. Right now, this is just a rectangle.
player = Player()
coins = pygame.sprite.Group()
clouds = pygame.sprite.Group()
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
        elif event.type == ADDCOIN:
            # Create the new enemy and add it to sprite groups
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
    # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
        
    for coin in coins:
        if player.rect.colliderect(coin):
            coin.kill()
            score+=1

    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    coins.update()
    clouds.update()

    # Draw the sky background
    screen.blit(sky_bg,(0,0))

    #Draw the hills
    screen.blit(hills_bg,(i,0))
    screen.blit(hills_bg,(SCREEN_WIDTH+i,0))
    if (i<-SCREEN_WIDTH):
        screen.blit(hills_bg,(SCREEN_WIDTH+i,0))
        i=0
    i -= game_speed

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
    game_speed=game_speed*.999