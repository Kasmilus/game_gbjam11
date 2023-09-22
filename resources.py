from typing import Tuple

from pyxel import blt, play, playm, pal

from constants import GRID_CELL_SIZE, HALF_GRID_CELL
from game_object import ObjType

IMAGE_SPLASH = 0
IMAGE_SPRITES = 1
IMAGE_UI = 2
IMAGE_TITLE = 2

SPRITE_UI_BOX = (0, 0)
SPRITE_UI_HOOK = (0, 2)
SPRITE_UI_COIN = (0, 3)
SPRITE_UI_KEY = (0, 4)
SPRITE_UI_CKPT = (0, 5)

SPRITE_SIZE = 16

SPRITE_PLAYER_IDLE = [(0, 0), (1, 0), (2, 0), (3, 0)]
SPRITE_PLAYER_RUN = [(6, 0), (7, 0), (8, 0), (9, 0), (10, 0)]
SPRITE_PLAYER_ROLL = [(6, 1), (7, 1), (8, 1), (9, 1)]
SPRITE_PLAYER_DEATH = [(12, 0), (13, 0), (14, 0), (15, 0)]
SPRITE_PLAYER_IDLE_SPEED = 120  # 2 sec per frame
SPRITE_PLAYER_RUN_SPEED = 7
SPRITE_PLAYER_ROLL_SPEED = 4
SPRITE_PLAYER_DEATH_SPEED = 5

SPRITE_ENEMY_FLYING_IDLE = [(0, 11), (1, 11), (2, 11), (3, 11)]
SPRITE_ENEMY_FLYING_RUN = SPRITE_ENEMY_FLYING_IDLE
SPRITE_ENEMY_FLYING_DEATH = [(5, 11), (6, 11), (7, 11), (8, 11)]
SPRITE_ENEMY_FLYING_IDLE_SPEED = 12
SPRITE_ENEMY_FLYING_RUN_SPEED = 8
SPRITE_ENEMY_FLYING_DEATH_SPEED = 4

SPRITE_ENEMY_WALKING_IDLE = [(0, 12), (1, 12), (2, 12), (3, 12)]
SPRITE_ENEMY_WALKING_RUN = [(5, 12), (6, 12), (7, 12), (8, 12)]
SPRITE_ENEMY_WALKING_DEATH = [(10, 12), (11, 12), (12, 12), (13, 12)]
SPRITE_ENEMY_WALKING_IDLE_SPEED = 12
SPRITE_ENEMY_WALKING_RUN_SPEED = 8
SPRITE_ENEMY_WALKING_DEATH_SPEED = 3

SPRITE_CHECKPOINT_ACTIVATION = [(0, 13), (1, 13), (2, 13), (3, 13)]

#
# SPRITES
#
ALL_OBJECTS = {
    "PLAYER": {'name': 'Player', "sprite": SPRITE_PLAYER_IDLE, "obj_type": ObjType.Player},
    "HOOK": {'name': 'Hook', 'sprite': [(0, 1), (1, 1), (2, 1), (3, 1)], "obj_type": ObjType.PlayerHook},

    'WALL_CORNER_LU': {'name': 'WallH', "sprite": (4, 7), "obj_type": ObjType.World, 'bounding_box': (0, 0, GRID_CELL_SIZE, GRID_CELL_SIZE-4)},
    'WALL_CORNER_RU': {'name': 'WallH', "sprite": (6, 7), "obj_type": ObjType.World, 'bounding_box': (0, 0, GRID_CELL_SIZE, GRID_CELL_SIZE-4)},
    'WALL_CORNER_LD': {'name': 'WallH', "sprite": (4, 9), "obj_type": ObjType.World, 'bounding_box': (0, 4, GRID_CELL_SIZE, GRID_CELL_SIZE-4)},
    'WALL_CORNER_RD': {'name': 'WallH', "sprite": (6, 9), "obj_type": ObjType.World, 'bounding_box': (0, 4, GRID_CELL_SIZE, GRID_CELL_SIZE-4)},
    'WALL_OPENING_LEFT_TOP': {'name': 'Wall', "sprite": (7, 8), "obj_type": ObjType.World, 'bounding_box': (0, 0, GRID_CELL_SIZE-6, GRID_CELL_SIZE)},
    'WALL_OPENING_LEFT_BOTTOM': {'name': 'Wall', "sprite": (7, 9), "obj_type": ObjType.World, 'bounding_box': (0, 2, GRID_CELL_SIZE-6, GRID_CELL_SIZE)},
    'WALL_OPENING_RIGHT_TOP': {'name': 'Wall', "sprite": (8, 8), "obj_type": ObjType.World, 'bounding_box': (6, 0, GRID_CELL_SIZE, GRID_CELL_SIZE)},
    'WALL_OPENING_RIGHT_BOTTOM': {'name': 'Wall', "sprite": (8, 9), "obj_type": ObjType.World, 'bounding_box': (6, 2, GRID_CELL_SIZE, GRID_CELL_SIZE)},
    'WALL_OPENING_DOWN_LEFT': {'name': 'WallH', "sprite": (4, 10), "obj_type": ObjType.World, 'bounding_box': (0, 5, GRID_CELL_SIZE, GRID_CELL_SIZE-4)},
    'WALL_OPENING_DOWN_RIGHT': {'name': 'WallH', "sprite": (5, 10), "obj_type": ObjType.World, 'bounding_box': (0, 5, GRID_CELL_SIZE, GRID_CELL_SIZE-4)},
    'WALL_UP': {'name': 'WallH', "sprite": (5, 7), "obj_type": ObjType.World, 'bounding_box': (0, 0, GRID_CELL_SIZE, GRID_CELL_SIZE-4)},
    'WALL_DOWN': {'name': 'WallH', "sprite": (5, 9), "obj_type": ObjType.World, 'bounding_box': (0, 5, GRID_CELL_SIZE, GRID_CELL_SIZE-4)},
    'WALL_LEFT': {'name': 'Wall', "sprite": (4, 8), "obj_type": ObjType.World, 'bounding_box': (0, 0, GRID_CELL_SIZE-6, GRID_CELL_SIZE)},
    'WALL_RIGHT': {'name': 'Wall', "sprite": (6, 8), "obj_type": ObjType.World, 'bounding_box': (6, 0, GRID_CELL_SIZE, GRID_CELL_SIZE)},

    'WATER_CORNER_LU': {'name': 'Water', "sprite": (0, 7), "obj_type": ObjType.Water},
    'WATER_CORNER_RU': {'name': 'Water', "sprite": (3, 7), "obj_type": ObjType.Water},
    'WATER_CORNER_LD': {'name': 'Water', "sprite": (0, 10), "obj_type": ObjType.Water},
    'WATER_CORNER_RD': {'name': 'Water', "sprite": (3, 10), "obj_type": ObjType.Water},
    'WATER_UP': {'name': 'Water', "sprite": (1, 7), "obj_type": ObjType.Water},
    'WATER_DOWN': {'name': 'Water', "sprite": (1, 10), "obj_type": ObjType.Water},
    'WATER_LEFT': {'name': 'Water', "sprite": (0, 8), "obj_type": ObjType.Water},
    'WATER_RIGHT': {'name': 'Water', "sprite": (3, 8), "obj_type": ObjType.Water},
    'WATER': {'name': 'Water', "sprite": (1, 9), "obj_type": ObjType.Water},

    'ENEMY_WALKING': {'name': 'Enemy Walking', 'sprite': SPRITE_ENEMY_WALKING_IDLE, "obj_type": ObjType.EnemyWalking, "is_hookable": False},
    'ENEMY_FLYING': {'name': 'Enemy Flying', 'sprite': SPRITE_ENEMY_FLYING_IDLE, "obj_type": ObjType.EnemyFlying, "is_hookable": True},

    'STONE_A': {'name': 'Stone', 'sprite': (0, 5), 'obj_type': ObjType.World, 'is_hookable': True, 'bounding_box': (1, 1, GRID_CELL_SIZE-1, GRID_CELL_SIZE-1)},
    'STONE_B': {'name': 'Stone', 'sprite': (3, 5), 'obj_type': ObjType.World, 'bounding_box': (1, 1, GRID_CELL_SIZE-1, GRID_CELL_SIZE-1)},
    'STONE_C': {'name': 'Stone', 'sprite': (4, 5), 'obj_type': ObjType.World, 'bounding_box': (1, 1, GRID_CELL_SIZE-1, GRID_CELL_SIZE-1)},
    'STONE_D': {'name': 'Stone', 'sprite': (2, 6), 'obj_type': ObjType.World, 'bounding_box': (1, 1, GRID_CELL_SIZE-1, GRID_CELL_SIZE-1)},
    'STONE_LARGE_00': {'name': 'LargeStone', 'sprite': (5, 5), 'obj_type': ObjType.World},
    'STONE_LARGE_10': {'name': 'LargeStone', 'sprite': (6, 5), 'obj_type': ObjType.World},
    'STONE_LARGE_01': {'name': 'LargeStone', 'sprite': (5, 6), 'obj_type': ObjType.World},
    'STONE_LARGE_11': {'name': 'LargeStone', 'sprite': (6, 6), 'obj_type': ObjType.World},


    'CHECKPOINT': {'name': 'Checkpoint', 'sprite': [(0, 13), (1, 13), (2, 13), (3, 13)], 'obj_type': ObjType.Checkpoint, 'bounding_box': (2, 3, GRID_CELL_SIZE-2, GRID_CELL_SIZE)},
    'COIN': {'name': 'Coin', 'sprite': [(0, 15), (1, 15), (2, 15), (3, 15), (4, 15)], 'obj_type': ObjType.Coin},
    'KEY': {'name': 'Key', 'sprite': [(0, 14), (1, 14), (2, 14), (3, 14)], 'obj_type': ObjType.Key},
    'DOOR': {'name': 'Door', 'sprite': (4, 14), 'obj_type': ObjType.Door, 'bounding_box': (0, 0, GRID_CELL_SIZE, GRID_CELL_SIZE-4)},
    'DOOR_STANDALONE': {'name': 'Door', 'sprite': (5, 14), 'obj_type': ObjType.Door, 'bounding_box': (0, 0, GRID_CELL_SIZE, GRID_CELL_SIZE - 1)},

    'LARGE_TREE_TOP': {'name': 'Large Tree (top)', "sprite": (1, 5), "obj_type": ObjType.World, 'bounding_box': (1, 10, GRID_CELL_SIZE-1, GRID_CELL_SIZE)},
    'LARGE_TREE_BOTTOM': {'name': 'Large Tree (bottom)', "sprite": (1, 6), "obj_type": ObjType.World, 'bounding_box': (1, 0, GRID_CELL_SIZE-1, GRID_CELL_SIZE-1)},
    'SMALL_TREE': {'name': 'Small Tree', "sprite": (2, 5), "obj_type": ObjType.World, 'bounding_box': (1, 1, GRID_CELL_SIZE-1, GRID_CELL_SIZE-1)},
    'LARGE_STONE_A': {'name': 'Extra Large Stone 1', "sprite": (5, 5), "obj_type": ObjType.World, 'collides': False},
    'LARGE_STONE_B': {'name': 'Extra Large Stone 2', "sprite": (6, 5), "obj_type": ObjType.World, 'collides': False},
    'LARGE_STONE_C': {'name': 'Extra Large Stone 3', "sprite": (5, 6), "obj_type": ObjType.World, 'collides': True},
    'LARGE_STONE_D': {'name': 'Extra Large Stone 4', "sprite": (6, 6), "obj_type": ObjType.World, 'collides': True},

    #
    # SPRITES - PARTICLES
    #
    'PARTICLE_RUN': {'name': 'Particle', "sprite": [(6, 2),(7, 2),(8, 2),(9, 2),(10, 2),(11, 2), (12, 3), (13, 2)], "obj_type": ObjType.ParticleRun},
    'PARTICLE_EXPLOSION': {'name': 'Particle', "sprite": [(8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5), (14, 5), (15, 5)], "obj_type": ObjType.ParticleExplosion},

    #
    # SPRITES - DECOR
    #
    'FLOWER_Q': {'name': 'Flower', "sprite": [(0, 2), (1, 2), (2, 2), (3, 2)], "obj_type": ObjType.Decor},
    'FLOWER_W': {'name': 'Flower', "sprite": [(0, 3), (1, 3), (2, 3), (3, 3)], "obj_type": ObjType.Decor},
    'FLOWER_E': {'name': 'Flower', "sprite": [(0, 4), (1, 4), (2, 4), (3, 4)], "obj_type": ObjType.Decor},

    'MUSHROOM_A': {'name': 'Mushroom', "sprite": (3, 4), "obj_type": ObjType.Decor},
    'MUSHROOM_B': {'name': 'Mushroom', "sprite": (4, 4), "obj_type": ObjType.Decor},
    'GRASS_H': {'name': 'Grass', "sprite": (5, 4), "obj_type": ObjType.Decor},
    'GRASS_J': {'name': 'Grass', "sprite": (6, 4), "obj_type": ObjType.Decor},
    'GRASS_K': {'name': 'Grass', "sprite": (7, 4), "obj_type": ObjType.Decor},
    'GRASS_L': {'name': 'Grass', "sprite": (8, 4), "obj_type": ObjType.Decor},
    'LITTLE_STONE': {'name': 'Tiny Stone', "sprite": (9, 4), "obj_type": ObjType.Decor},
}

SPRITE_WALL_CORNER_LU = (0, 5)
SPRITE_WALL_UP = (0, 5)





#
# SOUNDS
#
SOUND_PICK_COIN = 0
SOUND_PICK_KEY = 1
SOUND_HOOK_ATTACH = 2
SOUND_HOOK_THROW = 6
SOUND_ENEMY_DEATH_A = 3
SOUND_ENEMY_DEATH_B = 4
SOUND_INTRO_DROP = 9
SOUND_OPEN_DOOR = 10
SOUND_CHECKPOINT = 11
SOUND_GAME_OVER = 12
SOUND_ROLL = 13

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


def blt_sprite(spritesheet_pos: Tuple[int, int], x: int, y: int, transparent_color=0, invert: bool = False, invert_y: bool = False) -> None:
    size_x = SPRITE_SIZE
    size_y = SPRITE_SIZE
    if invert:
        size_x = -size_x
    if invert_y:
        size_y = -size_y

    blt(x, y, IMAGE_SPRITES,
        SPRITE_SIZE*spritesheet_pos[0], SPRITE_SIZE*spritesheet_pos[1],
        size_x, size_y, colkey=transparent_color)


def blt_splash(x: int, y: int) -> None:
    blt(x, y, IMAGE_SPLASH, 0, 0, 160, 144)

def blt_title(x: int, y: int) -> None:
    blt(x, y, IMAGE_TITLE, 0, 6*SPRITE_SIZE, 160, 144)


def blt_ui_sprite(spritesheet_pos: Tuple[int, int], size: Tuple[int, int], x: int, y: int, transparent_color=0) -> None:
    blt(x, y, IMAGE_UI,
        SPRITE_SIZE*spritesheet_pos[0], SPRITE_SIZE*spritesheet_pos[1],
        size[0], size[1], colkey=transparent_color)

def play_music(music: int) -> None:
    # In-game music should leave channel 1 for sounds
    #playm(music, loop=True)
    pass


def play_sound(sound: int, channel: int = 1) -> None:
    play(channel, sound)
    pass
