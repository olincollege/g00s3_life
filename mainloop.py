"""
run the game from this file
"""

#importing needed libraries
import sys
from game_assets import play_level
from game_assets import title_screen
from game_assets import end_screen
from game_assets import running
from game_assets import screen


# Main loop
while running:
    title_screen(screen)
    while True:
        play_level(screen)
        end_screen(screen)