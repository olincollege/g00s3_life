"""
This is where the character sprites are stored

"""
# Import the pygame module
import pygame
import random

#importing the screen size and height from constraints
from constraints import SCREEN_WIDTH
from constraints import SCREEN_HEIGHT

# importing the specific key inputs we need
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)


class Player(pygame.sprite.Sprite):
    """
    the payer class takes user input to update its position in the game

    """

    def __init__(self):
        """
        initializes player
        
        Args: self
        """
        super(Player, self).__init__()
        self.surf = pygame.image.load(
            "images/player_sprites/flygrey1.PNG").convert()
        self.surf = pygame.transform.scale(self.surf, (80, 48))
        badColor = self.surf.get_at((0, 0))
        self.surf.set_colorkey(badColor)
        self.rect = self.surf.get_rect()
        self.rect.y = SCREEN_HEIGHT/2
        self.rect.x = 100

    def update(self, pressed_keys):
        """
        updates position by taking user input
        when user presses a key it moves the character in designated direction
        args:
            self
            pressed_keys - user input, a specific key

        Returns: updated player position

        """
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


class RainbowPlayer(pygame.sprite.Sprite):
    """
    takes the same inputs as the player class
    a "re-skin" of the original g00se Life goose 
    """

    def __init__(self, x, y):
        """
        initializes the RainbowPlayer

        Args: 
            self
            x - the player's x position to swap out where goose should be
            y - the player's y position to swap out where goose should be

        """
        super(RainbowPlayer, self).__init__()
        self.surf = pygame.image.load(
            "images/player_sprites/rainbowfly.PNG").convert()
        self.surf = pygame.transform.scale(self.surf, (80, 48))
        badColor = self.surf.get_at((0, 0))
        self.surf.set_colorkey(badColor)
        self.rect = self.surf.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self, pressed_keys):
        """
        Args:
            self
            pressed_keys - user input, a specific key

        Returns: updated position of player

        """
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


class Enemy(pygame.sprite.Sprite):
    """
    Enemy sprite "spawns" in at random points
    also has random speed from 5-15
    """

    def __init__(self):
        """
        initializes enemy at random points

        Args: self

        """
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(
            "images/player_sprites/duck.png").convert()
        self.surf = pygame.transform.scale(self.surf, (40, 30))
        badColor = self.surf.get_at((0, 0))
        self.surf.set_colorkey(badColor)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 15)

    @property
    def self(self):
        return self

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        """
        updates current postion of enemy

        args: self

        """
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class BigCloud(pygame.sprite.Sprite):
    """
    Twice as big as the normal cloud
    The BigCloud is randomly generated at different places on the screen
    when the BigCloud moves off screen it is removed
    """

    def __init__(self):
        """
        initializes BigCloud

        Args: self

        """
        super(BigCloud, self).__init__()
        self.surf = pygame.image.load(
            "images/player_sprites/Goose_Life_Cloud.png").convert()
        self.surf = pygame.transform.scale(self.surf, (200, 200))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the BigCloud based on a constant speed
    # Remove the BigCloud when it passes the left edge of the screen
    def update(self):
        """
        updates BigCloud current position on screen 
        also removes BigCloud sprite if it passes left edge of screen

        Args: self
        """
        self.rect.move_ip(-2, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    """
    The cloud is randomly generated at different places on the screen
    """

    def __init__(self):
        """
        initializes cloud sprite

        Args: self

        """
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(
            "images/player_sprites/Goose_Life_Cloud.png").convert()
        self.surf = pygame.transform.scale(self.surf, (100, 100))
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
        """
        updates the cloud's position

        Args: self

        Returns: updated position of cloud

        """
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class Coin(pygame.sprite.Sprite):
    """
    the coin is randomly generated at different places on the screen
    when coin moves off of the screen the sprite gets removed

    """

    def __init__(self):
        """
        initializes coin 
        
        Args: self

        Returns: an interactable coin sprite at random points on the screen
        """
        super(Coin, self).__init__()
        self.surf = pygame.image.load(
            "images/player_sprites/coin.PNG").convert()
        self.surf = pygame.transform.scale(self.surf, (60, 60))
        #removing black background around the coin
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        """
        updates the position of the coin
        also removes coin sprite if it passes left edge of screen

        Args: self

        Returns: the updated position of coin

        """
        self.rect.move_ip(-3, 0)
        if self.rect.right < 0:
            self.kill()
