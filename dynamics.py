import pygame as pg
import pgzero as pgz
from pgzero.rect import Rect
from pgzero.actor import Actor
from pgzero.animation import animate
from pgzero.loaders import images
from pgzero import game
import data
import constants as cnst
import humanize
class ScalingActor(Actor):

    def __init__(self, image_name, pos):
        super().__init__(image_name, pos)
        self.scale = 1.0

    def draw(self):
        original_image = images.load(self.image)

        scaled_image = pg.transform.rotozoom(
            original_image,
            0,
            self.scale,
        )

        scaled_rect = scaled_image.get_rect(center=self.pos)

        game.screen.blit(scaled_image, scaled_rect.topleft)



def draw_dynamics(screen):
  
# Cookie
    #cookie image
    global cookie
    cookie = ScalingActor('cookie', pos=(cnst.width/6,cnst.height/2))
    cookie.draw()
    
    
    # Cookie Counter background
    num_cookies_bg_fill = pg.Surface((500, 80), pg.SRCALPHA)
    num_cookies_bg_fill.fill((0,0,0,80))
    screen.blit(num_cookies_bg_fill, (0, 170)) #transparent num cookies bg


## DYNAMIC ##

    # Cookie Counter
    screen.draw.text(
        f"{humanize.intword(data.raw_cookie_count, format='%g')} cookies",  # text
        center=(cnst.cookie_center_x,200),   # pos
        shadow=(1,1), scolor="#202020", # drop shadow
        color="white", fontname="merriweather_bold", fontsize=40 # font
    )  # num cookies
    screen.draw.text(
        f"per second: {humanize.intword(data.raw_cookie_rate, format='%g')}",  # text
        center=(cnst.cookie_center_x,232),   # pos
        shadow=(1,1), scolor="#202020", # drop shadow
        color="white", fontname="merriweather_bold", fontsize=15 # font
    )  # cookie_count

