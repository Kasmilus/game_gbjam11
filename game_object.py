from typing import List, Tuple, TypedDict, Optional
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
            self.player_hook_speed = 76  # Pixels per sec
            self.player_max_hooks = 1
            self.player_available_hooks = 1

        # Hook
        if obj_type == ObjType.PlayerHook:
            self.bounding_box = (6, 6, GRID_CELL_SIZE-6, GRID_CELL_SIZE-6)  # Smaller than sprite!
            self.draw_priority = 5
            self.hook_drag = 1  # slowdown per sec
            self.hook_moving_back = False
            self.hook_move_back_speed = 90

        # Enemies
        if obj_type == ObjType.Enemy:
            self.draw_priority = 4
            self.bounding_box = (5, 3, GRID_CELL_SIZE-5, GRID_CELL_SIZE-1)

    def get_pos(self) -> Tuple[int, int]:
        return self.pos_x, self.pos_y
    def get_pos_mid(self) -> Tuple[int, int]:
        return self.pos_x + HALF_GRID_CELL, self.pos_y + HALF_GRID_CELL
    def get_bbox_world_space(self) -> Tuple[int, int, int, int]:
        return self.pos_x + self.bounding_box[0], self.pos_y + self.bounding_box[1], self.pos_x + self.bounding_box[2], self.pos_y + self.bounding_box[3]


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


def _line_intersection_distance(x1, y1, x2, y2, x3, y3, x4, y4) -> Tuple[float, float]:
    denominator = ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))

    if denominator == 0:
        return -1, -1

    u_a = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator
    u_b = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator
    return u_a, u_b

def get_line_intersection_point(line_a_start: Tuple[float, float],line_a_end: Tuple[float, float], line_b_start: Tuple[float, float],line_b_end: Tuple[float, float],) -> Optional[Tuple[float, float]]:
    u_a, u_b = _line_intersection_distance(line_a_start[0], line_a_start[1], line_a_end[0], line_a_end[1],
                                           line_b_start[0], line_b_start[1], line_b_end[0], line_b_end[1])
    if 0 <= u_a <= 1 and 0 <= u_b <= 1:
        print("AAAAAAAAAA")
        intersection_x = line_a_start[0] + (u_a * (line_a_end[0]-line_a_start[0]))
        intersection_y = line_a_start[1] + (u_a * (line_a_end[1]-line_a_start[1]))
        return intersection_x, intersection_y

    return None

def get_line_bb_intersection_point(line_start: Tuple[float, float],line_end: Tuple[float, float], bb: Tuple[int, int, int, int],) -> Optional[Tuple[float, float]]:
    a = get_line_intersection_point(line_start, line_end, (bb[0], bb[1]), (bb[2], bb[1]))
    if a is not None:
        return a
    b = get_line_intersection_point(line_start, line_end, (bb[0], bb[1]), (bb[0], bb[3]))
    if b is not None:
        return b
    c = get_line_intersection_point(line_start, line_end, (bb[0], bb[3]), (bb[2], bb[3]))
    if c is not None:
        return c
    d = get_line_intersection_point(line_start, line_end, (bb[2], bb[1]), (bb[2], bb[3]))
    if d is not None:
        return d

    return None
