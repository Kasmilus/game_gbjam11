from typing import Tuple

from pyxel import blt, play, playm, pal

IMAGE_SPLASH = 0
IMAGE_SPRITES = 1

SPRITE_SIZE = 16

#
# SPRITES
#
SPRITE_PLAYER = (0, 0)

SPRITE_WALL_CORNER_LU = (0, 5)
SPRITE_WALL_UP = (0, 5)

SPRITE_STONE_A = (0, 5)
SPRITE_STONE_B = (3, 5)
SPRITE_STONE_C = (4, 5)
SPRITE_STONE_D = (2, 6)
SPRITE_STONE_LARGE_00 = (5, 5)
SPRITE_STONE_LARGE_10 = (6, 5)
SPRITE_STONE_LARGE_01 = (5, 6)
SPRITE_STONE_LARGE_11 = (6, 6)

SPRITES_HOOK = [(0, 1), (1, 1), (2, 1), (3, 1)]

SPRITE_ENEMY_A = (1, 11)

#
# SPRITES - DECOR
#
SPRITES_FLOWER_Q = [(0, 2), (1, 2), (2, 2), (3, 2)]
SPRITES_FLOWER_W = [(0, 3), (1, 3), (2, 3)]
SPRITES_FLOWER_E = [(0, 4), (1, 4), (2, 4)]
SPRITES_FLOWER_R = [(4, 3), (5, 3), (6, 3), (7, 3)]

#
# SOUNDS
#
SOUND_A = 0
SOUND_B = 1

#
# MUSIC
#
MUSIC_A = 0
MUSIC_B = 1

#
# COLORS
#
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
