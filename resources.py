from typing import Tuple

from pyxel import blt, play, playm, pal

IMAGE_SPLASH = 0
IMAGE_SPRITES = 1

SPRITE_SIZE = 16

SPRITE_PLAYER = (0, 0)

SPRITE_WALL_A = (0, 1)
SPRITE_WALL_B = (1, 1)

SOUND_A = 0
SOUND_B = 1

MUSIC_A = 0
MUSIC_B = 1

COLOR_BACKGROUND = 0
COLOR_MAIN = 6
COLOR_SECONDARY = 12
COLOR_DARK = 1


def flip_colors() -> None:
    pal(COLOR_BACKGROUND, COLOR_DARK)
    pal(COLOR_SECONDARY, COLOR_MAIN)
    pal(COLOR_DARK, COLOR_BACKGROUND)
    pal(COLOR_MAIN, COLOR_SECONDARY)


def reset_color() -> None:
    pal()


def blt_sprite(spritesheet_pos: Tuple[int, int], x: int, y: int, transparent_color=0) -> None:
    blt(x, y, IMAGE_SPRITES, SPRITE_SIZE*spritesheet_pos[0], SPRITE_SIZE*spritesheet_pos[1], SPRITE_SIZE, SPRITE_SIZE, colkey=transparent_color)


def blt_splash(x: int, y: int) -> None:
    blt(0, y, IMAGE_SPLASH, 0, 0, 160, 144)


def play_music(music: int) -> None:
    # In-game music should leave channel 1 for sounds
    #playm(music, loop=True)
    pass


def play_sound(sound: int) -> None:
    # Use channel 1 for sounds
    #play(1, sound)
    pass
