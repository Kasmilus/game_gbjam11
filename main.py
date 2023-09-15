import math
from typing import List, Tuple, TypedDict
from enum import Enum

import pyxel

from utils import *
import interp
from controls import Controls
import resources

# pyxel run main.py
# pyxel edit
# pyxel package . main.py
# pyxel app2html Pyxel.pyxapp
# pyxel app2exe Pyxel.pyxapp

FPS = 60
FRAME_TIME = 1/FPS

class GameState(Enum):
    Splash = 1,
    PressToStart = 2,
    Game = 3

class Obj:
    pos_x: int = 0
    pos_y: int = 0
    start_x: int = 0
    start_y: int = 0
    target_x: int = 0
    target_y: int = 0
    time: float = 0

    def __init__(self, color = resources.COLOR_MAIN, slerp=False):
        self.color = color
        self.slerp = slerp

class Game:
    #game_state: GameState = GameState.Game
    game_state: GameState = GameState.Splash
    objects: List[Obj] = []

    splash_timer: float = 0
    press_to_start_timer: float = 0

    camera_x: int = 0
    camera_y: int = 0

game: Game = Game()



def init():
    pyxel.init(160, 144, title="Game Name", fps=FPS, display_scale=3)
    pyxel.load("assets/my_resource.pyxres", image=True, tilemap=False, sound=True, music=True)

    game.objects.append(Obj(slerp=True, color=resources.COLOR_MAIN))
    game.objects.append(Obj(color=resources.COLOR_SECONDARY))
    game.objects.append(Obj(color=resources.COLOR_DARK))

    resources.play_music(resources.MUSIC_A)


def update():
    pyxel.camera(game.camera_x, game.camera_y)
    if Controls.down():
        game.camera_y += 1
    if Controls.down(True):
        resources.play_sound(resources.SOUND_A)

    #if pyxel.btn(pyxel.KEY_Q):
        #pyxel.quit()
    if game.game_state == GameState.Splash:
        game.splash_timer += FRAME_TIME
        if game.splash_timer > 1.5:
            game.game_state = GameState.PressToStart
    elif game.game_state == GameState.PressToStart:
        game.press_to_start_timer += FRAME_TIME
        if Controls.any():
            game.game_state = GameState.Game
        if game.press_to_start_timer > 1.2:
            game.press_to_start_timer = 0
    else:
        for obj in game.objects:
            #if Controls.left():
            #    obj.pos_x -= 1
            #if Controls.right():
            #    obj.pos_x += 1
            #if Controls.down():
            #    obj.pos_y -= 1
            #if Controls.up():
            #    obj.pos_y += 1
            if obj.time < 2.0:
                interp_type = interp.EasingType.Linear
                if obj.slerp:
                    interp_type = interp.EasingType.EaseOutElastic
                obj.pos_x = interp.interp(obj.start_x, obj.target_x, obj.time, 2.0, interp_type)
                obj.pos_y = interp.interp(obj.start_y, obj.target_y, obj.time, 2.0, interp_type)
                obj.time += FRAME_TIME
            else:
                obj.start_x = obj.pos_x
                obj.start_y = obj.pos_y
                obj.target_x = pyxel.rndi(-10, 170)
                obj.target_y = pyxel.rndi(-10, 150)
                obj.time = 0


def draw():
    pyxel.cls(resources.COLOR_BACKGROUND)
    if game.game_state == GameState.Splash:
        if game.splash_timer <= 1:
            y_pos = interp.interp(-144, 0, game.splash_timer, 1.0, easing=interp.EasingType.EaseOutBounce)
        else:
            y_pos = 0
        resources.blt_splash(0, y_pos)
    elif game.game_state == GameState.PressToStart:
        resources.blt_splash(0, 0)
        if game.press_to_start_timer < 0.8:
            pyxel.rect(25, 115, 110, 15, resources.COLOR_BACKGROUND)
            pyxel.rectb(25, 115, 110, 15, resources.COLOR_DARK)
            pyxel.text(31, 121, "PRESS ANY BUTTON TO START", resources.COLOR_DARK)
    elif game.game_state == GameState.Game:
        i = 0
        for obj in game.objects:
            for obj2 in game.objects:
                if obj is not obj2 and collision(obj.pos_x, obj.pos_y, obj2.pos_x, obj2.pos_y):
                    resources.flip_colors()
            resources.blt_sprite(resources.SPRITE_D, obj.pos_x, obj.pos_y)
            resources.reset_color()


init()
pyxel.run(update, draw)
