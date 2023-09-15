import math
from typing import List, Tuple
from enum import Enum

from game_object import Obj, ObjType
from constants import *
import resources
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
            if c == '0':
                continue
            elif c == '1':
                game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_A, pos=get_pos_for_room(cell_pos=(cell_pos_x, cell_pos_y), room_coords=room_coords)))
            elif c == '2':
                game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_B, pos=get_pos_for_room(cell_pos=(cell_pos_x, cell_pos_y), room_coords=room_coords)))
            else:
                raise Exception("Unknown cell type!")

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
