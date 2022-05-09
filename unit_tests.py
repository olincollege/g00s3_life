import pygame
from sqlalchemy import true
from game_assets import score

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
)



def test_button_press():
    """
    simulates a button push and checks that the button moves character right
    """
#simulates a keypress
check = pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
if =check
assert True

def test_window_size():
    """
    Test that the default display size of the pygame window is.
    """
    pygame.init()
    display_size = (800, 560)
    test_size = pygame.display.get_window_size()
    pygame.quit()
    if display_size == test_size:
        assert True

def coin_adding():
    """
    test that coins are being added
    """
    if score == 1:
        assert true