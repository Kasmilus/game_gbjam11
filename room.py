import math
from typing import List, Tuple
from enum import Enum

from game_object import Obj, ObjType
from constants import *
from resources import ALL_OBJECTS
import game


def get_pos_for_room(cell_pos: Tuple[int, int], room_coords: Tuple[int, int] = None) -> Tuple[int, int]:
    if room_coords is None:
        room_coords = get_current_room()
    room_origin = get_pos_from_room_coords(room_coords)
    return room_origin[0] + cell_pos[0] * GRID_CELL_SIZE, room_origin[1] + cell_pos[1] * GRID_CELL_SIZE


def create_room(layout: str, room_coords: Tuple[int, int], room_name: str) -> None:
    lines = layout.splitlines()
    assert len(lines) == ROOM_SIZE_Y
    for cell_pos_y, line in enumerate(lines):
        assert len(line) == ROOM_SIZE_X
        for cell_pos_x, c in enumerate(line):
            pos = get_pos_for_room(cell_pos=(cell_pos_x, cell_pos_y), room_coords=room_coords)
            new_obj = None
            add_decor = False

            if c == '0':
                continue
            elif c == '1':
                new_obj = Obj(**ALL_OBJECTS['WALL_CORNER_LU'], pos=pos)
            elif c == '2':
                new_obj = Obj(**ALL_OBJECTS['WALL_CORNER_RU'], pos=pos)
            elif c == '3':
                new_obj = Obj(**ALL_OBJECTS['WALL_CORNER_LD'], pos=pos)
                new_obj.draw_priority = 7
            elif c == '4':
                new_obj = Obj(**ALL_OBJECTS['WALL_CORNER_RD'], pos=pos)
                new_obj.draw_priority = 7
            elif c == '5':
                new_obj = Obj(**ALL_OBJECTS['WALL_UP'], pos=pos)
            elif c == '6':
                new_obj = Obj(**ALL_OBJECTS['WALL_DOWN'], pos=pos)
                new_obj.draw_priority = 7
            elif c == '7':
                new_obj = Obj(**ALL_OBJECTS['WALL_LEFT'], pos=pos)
            elif c == '8':
                new_obj = Obj(**ALL_OBJECTS['WALL_RIGHT'], pos=pos)
            elif c == 'z':
                new_obj = Obj(**ALL_OBJECTS['WALL_OPENING_LEFT_TOP'], pos=pos)
            elif c == 'x':
                new_obj = Obj(**ALL_OBJECTS['WALL_OPENING_LEFT_BOTTOM'], pos=pos)
            elif c == 'c':
                new_obj = Obj(**ALL_OBJECTS['WALL_OPENING_RIGHT_TOP'], pos=pos)
            elif c == 'v':
                new_obj = Obj(**ALL_OBJECTS['WALL_OPENING_RIGHT_BOTTOM'], pos=pos)
            elif c == 'b':
                new_obj = Obj(**ALL_OBJECTS['WALL_OPENING_DOWN_LEFT'], pos=pos)
            elif c == 'n':
                new_obj = Obj(**ALL_OBJECTS['WALL_OPENING_DOWN_RIGHT'], pos=pos)

            elif c == 't':
                new_obj = Obj(**ALL_OBJECTS['WATER_CORNER_LU'], pos=pos)
            elif c == 'y':
                new_obj = Obj(**ALL_OBJECTS['WATER_CORNER_RU'], pos=pos)
            elif c == 'u':
                new_obj = Obj(**ALL_OBJECTS['WATER_CORNER_LD'], pos=pos)
            elif c == 'i':
                new_obj = Obj(**ALL_OBJECTS['WATER_CORNER_RD'], pos=pos)
            elif c == '@':
                new_obj = Obj(**ALL_OBJECTS['WATER'], pos=pos)
            elif c == 'g':
                new_obj = Obj(**ALL_OBJECTS['WATER_UP'], pos=pos)
            elif c == 'h':
                new_obj = Obj(**ALL_OBJECTS['WATER_DOWN'], pos=pos)
            elif c == 'j':
                new_obj = Obj(**ALL_OBJECTS['WATER_LEFT'], pos=pos)
            elif c == 'k':
                new_obj = Obj(**ALL_OBJECTS['WATER_RIGHT'], pos=pos)

            elif c == 'q':
                new_obj = Obj(**ALL_OBJECTS['STONE_A'], pos=pos)
            elif c == 'w':
                new_obj = Obj(**ALL_OBJECTS['STONE_B'], pos=pos)
            elif c == 'e':
                new_obj = Obj(**ALL_OBJECTS['STONE_C'], pos=pos)
            elif c == 'r':
                new_obj = Obj(**ALL_OBJECTS['STONE_D'], pos=pos)

            elif c == '[':
                new_obj = Obj(**ALL_OBJECTS['LARGE_TREE_TOP'], pos=pos)
                new_obj.draw_priority = 7
            elif c == ']':
                new_obj = Obj(**ALL_OBJECTS['LARGE_TREE_BOTTOM'], pos=pos)
            elif c == '#':
                new_obj = Obj(**ALL_OBJECTS['SMALL_TREE'], pos=pos)
            elif c == 'o':
                new_obj = Obj(**ALL_OBJECTS['LARGE_STONE_A'], pos=pos)
                new_obj.draw_priority = 7
            elif c == 'p':
                new_obj = Obj(**ALL_OBJECTS['LARGE_STONE_B'], pos=pos)
                new_obj.draw_priority = 7
            elif c == '+':
                new_obj = Obj(**ALL_OBJECTS['LARGE_STONE_C'], pos=pos)
                new_obj.draw_priority = 7
            elif c == 'l':
                new_obj = Obj(**ALL_OBJECTS['LARGE_STONE_D'], pos=pos)
                new_obj.draw_priority = 7

            elif c == 'a':
                new_obj = Obj(**ALL_OBJECTS['CHECKPOINT'], pos=pos)
                new_obj.checkpoint_name = room_name
            elif c == 's':
                new_obj = Obj(**ALL_OBJECTS['COIN'], pos=pos)
            elif c == 'd':
                new_obj = Obj(**ALL_OBJECTS['KEY'], pos=pos)
            elif c == 'f':
                new_obj = Obj(**ALL_OBJECTS['DOOR'], pos=pos)
            elif c == 'D':
                new_obj = Obj(**ALL_OBJECTS['DOOR_STANDALONE'], pos=pos)

            elif c == 'T':
                new_obj = Obj(**ALL_OBJECTS['ENEMY_FLYING'], pos=pos)
            elif c == 'Y':
                new_obj = Obj(**ALL_OBJECTS['ENEMY_WALKING'], pos=pos)
            #
            # Decor
            #
            elif c == 'Q':
                new_obj = Obj(**ALL_OBJECTS['FLOWER_Q'], pos=pos)
                new_obj.anim_speed = 115
                add_decor = True
            elif c == 'W':
                new_obj = Obj(**ALL_OBJECTS['FLOWER_W'], pos=pos)
                new_obj.anim_speed = 94
                add_decor = True
            elif c == 'E':
                new_obj = Obj(**ALL_OBJECTS['FLOWER_E'], pos=pos)
                new_obj.anim_speed = 238
                add_decor = True
            elif c == 'R':
                new_obj = Obj(**ALL_OBJECTS['LITTLE_STONE'], pos=pos)
                add_decor = True
            elif c == 'F':
                new_obj = Obj(**ALL_OBJECTS['MUSHROOM_A'], pos=pos)
                add_decor = True
            elif c == 'G':
                new_obj = Obj(**ALL_OBJECTS['MUSHROOM_B'], pos=pos)
                add_decor = True
            elif c == 'H':
                new_obj = Obj(**ALL_OBJECTS['GRASS_H'], pos=pos)
                add_decor = True
            elif c == 'J':
                new_obj = Obj(**ALL_OBJECTS['GRASS_J'], pos=pos)
                add_decor = True
            elif c == 'K':
                new_obj = Obj(**ALL_OBJECTS['GRASS_K'], pos=pos)
                add_decor = True
            elif c == 'L':
                new_obj = Obj(**ALL_OBJECTS['GRASS_L'], pos=pos)
                add_decor = True
            else:
                raise Exception(f"Unknown cell type: {c}!")

            assert type(new_obj) is Obj
            if add_decor is True:
                game.game.objects_decor.append(new_obj)
            else:
                game.game.all_objects.append(new_obj)

def get_room_from_pos(pos: Tuple[int, int]) -> Tuple[int, int]:
    cell_coord = round(pos[0] / GRID_CELL_SIZE), round(pos[1] / GRID_CELL_SIZE)
    room_coord = math.floor(cell_coord[0] / ROOM_SIZE_X), math.floor(cell_coord[1] / ROOM_SIZE_Y)
    return room_coord

def get_pos_from_room_coords(room_coords: Tuple[int, int]) -> Tuple[int, int]:
    pos = room_coords[0] * ROOM_SIZE_X * GRID_CELL_SIZE, room_coords[1] * ROOM_SIZE_Y * GRID_CELL_SIZE
    return pos

def move_camera_to_new_room(room_coords: Tuple[int, int]) -> None:
    game.game.camera_target_x, game.game.camera_target_y = get_pos_from_room_coords(room_coords)
    game.game.camera_move_timer = 0


def get_current_room() -> Tuple[int, int]:
    return get_room_from_pos((game.game.camera_target_x, game.game.camera_target_y))

def update_current_room_objects():
    # First clear all static objects
    remove_list = []
    for obj in game.game.objects:
        if obj.obj_type not in [ObjType.Player, ObjType.PlayerHook, ObjType.EnemyFlying, ObjType.EnemyWalking]:
            remove_list.append(obj)
    for obj in remove_list:
        game.game.objects.remove(obj)

    # Add objects from nearby rooms
    current_room = get_current_room()
    for obj in game.game.all_objects:
        if obj not in game.game.objects:
            obj_room = get_room_from_pos(obj.get_pos())
            if (current_room[0] - 2 <= obj_room[0] <= current_room[0] + 2) and current_room[1] == obj_room[1]:
                game.game.objects.append(obj)
            elif (current_room[1] - 2 <= obj_room[1] <= current_room[1] + 2) and current_room[0] == obj_room[0]:
                game.game.objects.append(obj)
