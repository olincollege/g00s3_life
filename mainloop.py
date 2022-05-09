"""
Run the game from this file
"""

# importing needed libraries
from game_assets import play_level
from game_assets import title_screen
from game_assets import end_screen
from game_assets import screen

#Starts with the title screen
title_screen(screen)

#Loops between game and end/retry screen
while True:
    final_score = play_level(screen)
    end_screen(screen, final_score)
