from typing import Tuple

from pyxel import blt, play, playm, pal

from game_object import ObjType

IMAGE_SPLASH = 0
IMAGE_SPRITES = 1

SPRITE_SIZE = 16

SPRITE_PLAYER_IDLE = [(0, 0), (1, 0), (2, 0), (3, 0)]
SPRITE_PLAYER_RUN = [(6, 0), (7, 0), (8, 0), (9, 0), (10, 0)]
SPRITE_PLAYER_ROLL = [(6, 1), (7, 1), (8, 1), (9, 1)]
SPRITE_PLAYER_DEATH = [(12, 0), (13, 0), (14, 0), (15, 0)]
SPRITE_PLAYER_IDLE_SPEED = 120  # 2 sec per frame
SPRITE_PLAYER_RUN_SPEED = 7
SPRITE_PLAYER_ROLL_SPEED = 4
SPRITE_PLAYER_DEATH_SPEED = 5

SPRITE_CHECKPOINT_ACTIVATION = [(0, 13), (1, 13), (2, 13), (3, 13)]
#
# SPRITES
#
ALL_OBJECTS = {
    "PLAYER": {'name': 'Player', "sprite": SPRITE_PLAYER_IDLE, "obj_type": ObjType.Player},
    "HOOK": {'name': 'Hook', 'sprite': [(0, 1), (1, 1), (2, 1), (3, 1)], "obj_type": ObjType.PlayerHook},

    'WALL_CORNER_LU': {'name': 'Wall', "sprite": (4, 7), "obj_type": ObjType.World},
    'WALL_CORNER_RU': {'name': 'Wall', "sprite": (6, 7), "obj_type": ObjType.World},
    'WALL_CORNER_LD': {'name': 'Wall', "sprite": (4, 9), "obj_type": ObjType.World},
    'WALL_CORNER_RD': {'name': 'Wall', "sprite": (6, 9), "obj_type": ObjType.World},
    'WALL_OPENING_LEFT_TOP': {'name': 'Wall', "sprite": (7, 8), "obj_type": ObjType.World},
    'WALL_OPENING_LEFT_BOTTOM': {'name': 'Wall', "sprite": (7, 9), "obj_type": ObjType.World},
    'WALL_OPENING_RIGHT_TOP': {'name': 'Wall', "sprite": (8, 8), "obj_type": ObjType.World},
    'WALL_OPENING_RIGHT_BOTTOM': {'name': 'Wall', "sprite": (8, 9), "obj_type": ObjType.World},
    'WALL_OPENING_DOWN_LEFT': {'name': 'Wall', "sprite": (4, 10), "obj_type": ObjType.World},
    'WALL_OPENING_DOWN_RIGHT': {'name': 'Wall', "sprite": (5, 10), "obj_type": ObjType.World},
    'WALL_UP': {'name': 'Wall', "sprite": (5, 7), "obj_type": ObjType.World},
    'WALL_DOWN': {'name': 'Wall', "sprite": (5, 9), "obj_type": ObjType.World},
    'WALL_LEFT': {'name': 'Wall', "sprite": (4, 8), "obj_type": ObjType.World},
    'WALL_RIGHT': {'name': 'Wall', "sprite": (6, 8), "obj_type": ObjType.World},

    'ENEMY_A': {'name': 'EnemyA', 'sprite': (0, 11), "obj_type": ObjType.Enemy, "is_hookable": True},
    'ENEMY_B': {'name': 'EnemyB', 'sprite': (1, 11), "obj_type": ObjType.Enemy, "is_hookable": True},

    'STONE_A': {'name': 'Stone', 'sprite': (0, 5), 'obj_type': ObjType.World, 'is_hookable': True},
    'STONE_B': {'name': 'Stone', 'sprite': (3, 5), 'obj_type': ObjType.World},
    'STONE_C': {'name': 'Stone', 'sprite': (4, 5), 'obj_type': ObjType.World},
    'STONE_D': {'name': 'Stone', 'sprite': (2, 6), 'obj_type': ObjType.World},
    'STONE_LARGE_00': {'name': 'LargeStone', 'sprite': (5, 5), 'obj_type': ObjType.World},
    'STONE_LARGE_10': {'name': 'LargeStone', 'sprite': (6, 5), 'obj_type': ObjType.World},
    'STONE_LARGE_01': {'name': 'LargeStone', 'sprite': (5, 6), 'obj_type': ObjType.World},
    'STONE_LARGE_11': {'name': 'LargeStone', 'sprite': (6, 6), 'obj_type': ObjType.World},


    'CHECKPOINT': {'name': 'Checkpoint', 'sprite': [(0, 13), (1, 13), (2, 13), (3, 13)], 'obj_type': ObjType.Checkpoint},
    'COIN': {'name': 'Coin', 'sprite': [(0, 15), (1, 15), (2, 15), (3, 15), (4, 15)], 'obj_type': ObjType.Coin},
    'KEY': {'name': 'Key', 'sprite': [(0, 14), (1, 14), (2, 14), (3, 14)], 'obj_type': ObjType.Key},
    'DOOR': {'name': 'Door', 'sprite': (4, 14), 'obj_type': ObjType.Door},

    #
    # SPRITES - DECOR
    #
    'FLOWER_Q': {'name': 'Flower', "sprite": [(0, 2), (1, 2), (2, 2), (3, 2)], "obj_type": ObjType.Decor},
    'FLOWER_W': {'name': 'Flower', "sprite": [(0, 3), (1, 3), (2, 3)], "obj_type": ObjType.Decor},
    'FLOWER_E': {'name': 'Flower', "sprite": [(0, 4), (1, 4), (2, 4)], "obj_type": ObjType.Decor},
    'FLOWER_R': {'name': 'Flower', "sprite": [(4, 3), (5, 3), (6, 3), (7, 3)], "obj_type": ObjType.Decor},
}

SPRITE_WALL_CORNER_LU = (0, 5)
SPRITE_WALL_UP = (0, 5)





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


def blt_sprite(spritesheet_pos: Tuple[int, int], x: int, y: int, transparent_color=0, invert: bool = False) -> None:
    size = SPRITE_SIZE
    pos_add = 0
    if invert:
        size = -size

    blt(x, y, IMAGE_SPRITES,
        SPRITE_SIZE*spritesheet_pos[0], SPRITE_SIZE*spritesheet_pos[1],
        size, SPRITE_SIZE, colkey=transparent_color)


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
