from typing import List, Tuple, TypedDict
from enum import Enum

from constants import *

class ObjType(Enum):
    Undefined = 0
    Player = 1
    Enemy = 2
    World = 3
    PlayerHook = 4


class Obj:
    def __init__(self, obj_type: ObjType, sprite: Tuple[int, int], pos: Tuple[int, int]):
        self.obj_type = obj_type
        self.sprite = sprite
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.last_move_dir = (1, 0)  # Always start facing right
        self.hook_velocity = None  # hook only

        self.bounding_box = (0, 0, GRID_CELL_SIZE, GRID_CELL_SIZE)
        self.draw_priority = 0  # The higher, the later it will be drawn (on top of others)

        # Player specific
        if obj_type == ObjType.Player:
            self.bounding_box = (5, 2, GRID_CELL_SIZE-5, GRID_CELL_SIZE-1)
            self.draw_priority = 3
            self.player_speed = 0
            self.player_dash_timer = 0
            self.player_hook_speed = 64  # Pixels per sec
            self.player_max_hooks = 1
            self.player_available_hooks = 1

        # Hook
        if obj_type == ObjType.PlayerHook:
            self.bounding_box = (6, 6, GRID_CELL_SIZE-6, GRID_CELL_SIZE-6)  # Smaller than sprite!
            self.draw_priority = 5
            self.hook_drag = 1  # slowdown per sec

        # Enemies
        if obj_type == ObjType.Enemy:
            self.draw_priority = 4
            self.bounding_box = (5, 3, GRID_CELL_SIZE-5, GRID_CELL_SIZE-1)

    def get_pos(self) -> Tuple[int, int]:
        return self.pos_x, self.pos_y


def collision_bb(pos_a: Tuple[int, int], bb_a: Tuple[int, int, int, int], pos_b: Tuple[int, int], bb_b: Tuple[int, int, int, int]) -> bool:
    collides = pos_a[0] + bb_a[0] < pos_b[0] + bb_b[2] and \
               pos_a[0] + bb_a[2] > pos_b[0] + bb_b[0] and \
               pos_a[1] + bb_a[1] < pos_b[1] + bb_b[3] and \
               pos_a[1] + bb_a[3] > pos_b[1] + bb_b[1]
    return collides


def collision_obj(obj_a: Obj, obj_b: Obj) -> bool:
    if obj_a is obj_b:
        return False
    return collision_bb(obj_a.get_pos(), obj_a.bounding_box, obj_b.get_pos(), obj_b.bounding_box)
