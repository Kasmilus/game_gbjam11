import math
from typing import List, Tuple
from enum import Enum

from game_object import Obj, ObjType
from constants import *
from resources import ALL_OBJECTS
from game import game


def get_pos_for_room(cell_pos: Tuple[int, int], room_coords: Tuple[int, int] = None) -> Tuple[int, int]:
    if room_coords is None:
        room_coords = get_current_room()
    room_origin = get_pos_from_room_coords(room_coords)
    return room_origin[0] + cell_pos[0] * GRID_CELL_SIZE, room_origin[1] + cell_pos[1] * GRID_CELL_SIZE


def create_room(layout: str, room_coords: Tuple[int, int]) -> None:
    lines = layout.splitlines()
    assert len(lines) == ROOM_SIZE_Y
    for cell_pos_y, line in enumerate(lines):
        assert len(line) == ROOM_SIZE_X
        for cell_pos_x, c in enumerate(line):
            pos = get_pos_for_room(cell_pos=(cell_pos_x, cell_pos_y), room_coords=room_coords)
            new_obj = None

            if c == '0':
                continue
            elif c == '1':
                new_obj = Obj(**ALL_OBJECTS['WALL_CORNER_LU'], pos=pos)
            elif c == '2':
                new_obj = Obj(**ALL_OBJECTS['WALL_CORNER_RU'], pos=pos)
            elif c == '3':
                new_obj = Obj(**ALL_OBJECTS['WALL_CORNER_LD'], pos=pos)
            elif c == '4':
                new_obj = Obj(**ALL_OBJECTS['WALL_CORNER_RD'], pos=pos)
            elif c == '5':
                new_obj = Obj(**ALL_OBJECTS['WALL_UP'], pos=pos)
            elif c == '6':
                new_obj = Obj(**ALL_OBJECTS['WALL_DOWN'], pos=pos)
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

            elif c == 'q':
                new_obj = Obj(**ALL_OBJECTS['STONE_A'], pos=pos)
            elif c == 'w':
                new_obj = Obj(**ALL_OBJECTS['STONE_B'], pos=pos)
            elif c == 'e':
                new_obj = Obj(**ALL_OBJECTS['STONE_C'], pos=pos)
            elif c == 'r':
                new_obj = Obj(**ALL_OBJECTS['STONE_D'], pos=pos)
            #
            # Decor
            #
            elif c == 'Q':
                new_obj = Obj(**ALL_OBJECTS['FLOWER_Q'], pos=pos)
                new_obj.anim_speed = 35
            elif c == 'W':
                new_obj = Obj(**ALL_OBJECTS['FLOWER_W'], pos=pos)
                new_obj.anim_speed = 32
            elif c == 'E':
                new_obj = Obj(**ALL_OBJECTS['FLOWER_E'], pos=pos)
                new_obj.anim_speed = 38
            elif c == 'R':
                new_obj = Obj(**ALL_OBJECTS['FLOWER_R'], pos=pos)
                new_obj.anim_speed = 30
            else:
                raise Exception("Unknown cell type!")

            assert type(new_obj) is Obj
            game.objects.append(new_obj)

def get_room_from_pos(pos: Tuple[int, int]) -> Tuple[int, int]:
    cell_coord = round(pos[0] / GRID_CELL_SIZE), round(pos[1] / GRID_CELL_SIZE)
    room_coord = math.floor(cell_coord[0] / ROOM_SIZE_X), math.floor(cell_coord[1] / ROOM_SIZE_Y)
    return room_coord

def get_pos_from_room_coords(room_coords: Tuple[int, int]) -> Tuple[int, int]:
    pos = room_coords[0] * ROOM_SIZE_X * GRID_CELL_SIZE, room_coords[1] * ROOM_SIZE_Y * GRID_CELL_SIZE
    return pos

def move_camera_to_new_room(room_coords: Tuple[int, int]) -> None:
    game.camera_target_x, game.camera_target_y = get_pos_from_room_coords(room_coords)
    game.camera_move_timer = 0

def get_current_room() -> Tuple[int, int]:
    return get_room_from_pos((game.camera_target_x, game.camera_target_y))
