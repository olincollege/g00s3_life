# Import the pygame module and random module
import pygame
import random 

# Import pygame locals for easier access
from pygame.locals import (
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# Define the constants for the screen
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

# Create some variables for jumping 
is_jump = False
jump_count = 10
enemy_jump_count = 10

# Define a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.top = 400
        self.rect.left = 50
    
    def update(self, pressed_keys):
        global is_jump, jump_count, jump_negative
        if not(is_jump):
            jump_negative = 1
            if jump_count < 0:
                jump_negative = -1
            if pressed_keys[K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -10:
                jump_negative = 1
                if jump_count < 0:
                    jump_negative = -1
                self.rect.move_ip(0, -0.6 * jump_count ** 2 * jump_negative)
                jump_count -= 1 
            else:
                is_jump = False
                jump_count = 10

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
        center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH+100),
                400
            )
        )
        self.speed = random.randint(5, 15)

    def update(self):
        global enemy_jump_count

        if enemy_jump_count >= -10:
            enemy_jump_negative = 1
            if enemy_jump_count < 0:
                enemy_jump_negative = -1
            self.rect.move_ip(-self.speed,-0.1 * enemy_jump_count ** 2 * enemy_jump_negative)
            enemy_jump_count -= 1
        else:
            enemy_jump_count = 10
        if self.rect.right < 0:
            self.kill()

# Initialize the pygame module
pygame.init()

# Create the screen object.
# Width and height are determined by SCREEN_WIDTH and SCREEN_HEIGHT respectively
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)

# Instantiate the player
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep the main loop running
running = True

# Main loop
while running == True:
    # Look at every event in queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Did the user hit the escape key?
            if event.key == K_ESCAPE:
                running = False
        
        # Did the user hit the window close button?
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to the sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()

    # Fill the screen with white
    screen.fill((0, 0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        #If so, then remove the player and stop the loop
        player.kill()
        running = False

    # Update the display
    pygame.display.flip()
