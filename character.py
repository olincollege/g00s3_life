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
    K_DOWN
)


class Player(pygame.sprite.Sprite):
    """
    insert docstring here plz
    """
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images/player_sprites/flygrey1.PNG").convert()
        self.surf = pygame.transform.scale(self.surf, (80, 48))
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




class Enemy(pygame.sprite.Sprite):
    """
    insert docstring here plz
    """
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((0, 0, 255))
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



class Cloud(pygame.sprite.Sprite):
    """
    insert docstring here plz
    """
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("images/player_sprites/Goose_Life_Cloud.png").convert()
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
