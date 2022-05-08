"""
stores functions and classes we call in order to play the game

"""
#importing needed libraries
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import sys

# Import the pygame module
import pygame
from constraints import SCREEN_WIDTH
from constraints import SCREEN_HEIGHT
from character import Player
from character import Enemy
from character import Cloud
from character import Coin

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    #RLEACCEL,
    #K_UP,
    #K_DOWN,
    #K_LEFT,
    #K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#defining variables
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
sky_bg = pygame.image.load('images/Goose_Life_Skybox.png')
sky_bg = pygame.transform.scale(sky_bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
sky_bg = pygame.transform.rotate(sky_bg,180)
hills_bg = pygame.image.load('images/Goose_Life_Rolling_Background_2.png')
hills_bg = pygame.transform.scale(hills_bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
transColor = hills_bg.get_at((0,0))
hills_bg.set_colorkey(transColor)
clock = pygame.time.Clock()
player = Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
running = True
WHITE = (255, 255, 255)
bg = pygame.image.load('images/titlescreen.PNG')
# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1500)
ADDCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCOIN, round(1500/5))


all_sprites.add(player)
# Variable to keep the main loop running


#initializing pygame
pygame.init()


#first function
def play_level(screen):
    """

    Args:

    Returns: Runs the main game

    """
    i = 0
    score = 0
     # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                game_state = game_state.QUIT
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            game_state = game_state.QUIT

    # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

        elif event.type == ADDCOIN:
            # Create the new enemy and add it to sprite groups
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    for coin in coins:
        if player.rect.colliderect(coin):
            coin.kill()
            score+=1


    if pygame.sprite.spritecollideany(player, enemies):
    # If so, then remove the player and stop the loop
        player.kill()
        sys.exit() #exits game when player dead

    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()
    clouds.update()

    #update coins
    coins.update()

    # Draw the sky background
    screen.blit(sky_bg,(0,0))

    #Draw the hills
    screen.blit(hills_bg,(i,0))
    screen.blit(hills_bg,(SCREEN_WIDTH+i,0))
    if i==-SCREEN_WIDTH:
        screen.blit(hills_bg,(SCREEN_WIDTH+i,0))
        i=0
    i -= 1

    # Draw the player on the screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, (255, 255, 255))
    screen.blit(text, (250,10))


    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 60 frames per second
    clock.tick(60)







def create_surface_with_text(text, font_size, text_rgb):
    """
    this function Returns surface with text written on

    Args:
        text - text you want
        font_size - size you want text
        text_rgb - colour of the text


    Returns: surface with text written on

    """

    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """
    An user interface element that can be added to a surface.

    """

    def __init__(self, center_position, text, font_size,text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            text_rgb (text colour) - tuple (r, g, b)
        """
        self.mouse_over = False  # indicates if the mouse is over the element
        self.action = action
        # create the default image
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb
        )

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # calls the init method of the parent sprite class
        super().__init__()

    # properties that vary the image and its rect when the mouse is over the element
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """
         Draws element onto a surface
        """
        surface.blit(self.image, self.rect)


# call main when the script is run
#if __name__ == "__main__":
    #main()


class game_state(Enum):
    """
    defining game_state as a class

    Returns:
    """
    QUIT = -1
    TITLE = 0
    NEWGAME = 1

#making sure that the game state starts at 0 (the title screen)
game_state = game_state.TITLE









def title_screen(screen):
    pygame.image.load('images/titlescreen.PNG')
    start_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        text_rgb=WHITE,
        text="Start",
        action= game_state.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        text_rgb=WHITE,
        text="Quit",
        action= game_state.QUIT,
    )

    buttons = [start_btn, quit_btn]
    pygame.image.load('images/titlescreen.PNG')
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.blit(bg,(0,0))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
