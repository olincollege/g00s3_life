"""
This is where the characters are stored

"""
# Import the pygame module
import pygame
import random

#importing the screen size and height from game.py
from constraints import SCREEN_WIDTH
from constraints import SCREEN_HEIGHT

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)


class Player(pygame.sprite.Sprite):
    """
    insert docstring here plz
    """
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images/player_sprites/flygrey1.PNG").convert()
        self.surf = pygame.transform.scale(self.surf, (80, 48))
        badColor = self.surf.get_at((0,0))
        self.surf.set_colorkey(badColor)
        self.rect = self.surf.get_rect()
        self.rect.y = SCREEN_HEIGHT/2
        self.rect.x = 100

    def update(self, pressed_keys):
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
    insert docstring here plz
    """
    def __init__(self, x, y):
        super(RainbowPlayer, self).__init__()
        self.surf = pygame.image.load("images/player_sprites/rainbowfly.PNG").convert()
        self.surf = pygame.transform.scale(self.surf, (80, 48))
        badColor = self.surf.get_at((0,0))
        self.surf.set_colorkey(badColor)
        self.rect = self.surf.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self, pressed_keys):
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
    insert docstring here plz
    """
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("images/player_sprites/duck.png").convert()
        self.surf = pygame.transform.scale(self.surf, (40,30))
        badColor = self.surf.get_at((0,0))
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
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class BigCloud(pygame.sprite.Sprite):
    """
    insert docstring here plz
    """
    def __init__(self):
        super(BigCloud, self).__init__()
        self.surf = pygame.image.load("images/player_sprites/Goose_Life_Cloud.png").convert()
        self.surf = pygame.transform.scale(self.surf, (200, 200))
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
        self.rect.move_ip(-2, 0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    """
    insert docstring here plz
    """
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("images/player_sprites/Goose_Life_Cloud.png").convert()
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
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()



class Coin(pygame.sprite.Sprite):
    """
    add docstring plz
    """
    def __init__(self):
        super(Coin, self).__init__()
        self.surf = pygame.image.load("images/player_sprites/coin.PNG").convert()
        self.surf = pygame.transform.scale(self.surf, (60, 60))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-3, 0)
        if self.rect.right < 0:
            self.kill()
