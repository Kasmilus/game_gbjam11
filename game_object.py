from typing import List, Tuple, TypedDict
from enum import Enum


class ObjType(Enum):
    Undefined = 0
    Player = 1
    Enemy = 2
    World = 3


class Obj:
    def __init__(self, obj_type: ObjType, sprite: Tuple[int, int], pos: Tuple[int, int]):
        self.obj_type = obj_type
        self.sprite = sprite
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.collisions: List[Obj] = []

        # Player specific
        self.player_speed = 0
        self.player_dash_timer = 0
