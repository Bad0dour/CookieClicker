import os
os.environ["SDL_VIDEO_CENTERED"] = "1"
import pgzrun as pgz
import constants
import data
import dynamics

WIDTH = constants.width
HEIGHT = constants.height
cookie_held = False


def draw():
    screen.blit("background", (0,0))
    dynamics.draw_dynamics(screen)

def on_mouse_up(pos):
    if dynamics.cookie.collidepoint(pos):
        print("clicked cookie")
        data.raw_cookie_count += 1
        print(data.raw_cookie_count)
        
pgz.go()