from typing import Tuple

from pyxel import blt, play, playm

IMAGE_SPLASH = 0
IMAGE_SPRITES = 1

SPRITE_SIZE = 16
SPRITE_A = (1, 0)
SPRITE_B = (2, 0)
SPRITE_C = (1, 1)
SPRITE_D = (2, 1)

SOUND_A = 0
SOUND_B = 1

MUSIC_A = 0
MUSIC_B = 1


def blt_sprite(sprite_pos: Tuple[int, int], x: int, y: int) -> None:
    blt(x, y, IMAGE_SPRITES, SPRITE_SIZE*sprite_pos[0], SPRITE_SIZE*sprite_pos[1], SPRITE_SIZE, SPRITE_SIZE, colkey=0)


def blt_splash(x: int, y: int) -> None:
    blt(0, y, IMAGE_SPLASH, 0, 0, 160, 144)


def play_music(music: int) -> None:
    # In-game music should leave channel 1 for sounds
    playm(music, loop=True)


def play_sound(sound: int) -> None:
    # Use channel 1 for sounds
    play(1, sound)
