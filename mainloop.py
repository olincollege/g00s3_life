"""
run the game from this file
"""

#importing needed libraries
import sys
from game_assets import play_level
from game_assets import title_screen
from game_assets import running
from game_assets import screen
from game_assets import game_state


# Main loop
while running:

    if game_state == game_state.TITLE:
        game_state = title_screen(screen)


    if game_state == game_state.NEWGAME:
        play_level(screen)


    if game_state == game_state.QUIT:
        running = False
        sys.exit() #exits game completely
