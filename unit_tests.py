"""
this file contains our unit tests
"""
import pytest
import pygame
import character

from constraints import *


# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Initialize one of each type for testing
test_player = character.Player()


@pytest.mark.parametrize("actual,expected", [
    (test_player.rect.x, 100),
    (test_player.rect.height, 48),
    (test_player.rect.width, 80)
])

def test_player(actual, expected):
    assert actual == expected


@pytest.mark.parametrize("actual,expected", [
    (screen.get_width(), 800),
    (screen.get_height(), 560)
])
def test_screen(actual, expected):
    assert actual == expected
