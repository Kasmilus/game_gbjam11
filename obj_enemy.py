import math
from typing import List, Tuple
from enum import Enum

import pyxel

from constants import *
from room import *
import room_layouts
from utils import *
import interp
from controls import Controls
import resources
import game_object
from game import *

def kill_enemy(obj: Obj):
    game.objects.append(Obj(pos=obj.get_pos(), **resources.ALL_OBJECTS['PARTICLE_EXPLOSION']))
    if obj.obj_type is ObjType.EnemyFlying:
        obj.sprite = resources.SPRITE_ENEMY_FLYING_DEATH
        obj.anim_speed = resources.SPRITE_ENEMY_FLYING_DEATH_SPEED + pyxel.rndi(0, 2)
    elif obj.obj_type is ObjType.EnemyWalking:
        obj.sprite = resources.SPRITE_ENEMY_WALKING_DEATH
        obj.anim_speed = resources.SPRITE_ENEMY_WALKING_DEATH_SPEED + pyxel.rndi(0, 2)
    obj.death_timer = obj.anim_speed * len(obj.sprite)
    game.stop_frames = 3


def update_enemy_common(obj: Obj, destroy_list: List[Obj]):
    if obj.collided_during_hook is True and obj.death_timer is None:
        # Initiate death anim
        kill_enemy(obj)
        for obj2 in game.objects:
            # TODO: kill player, destroy nearby rocks
            if obj2.obj_type in [ObjType.EnemyFlying, ObjType.EnemyWalking]:
                if game_object.get_dist_obj(obj, obj2) < (GRID_CELL_SIZE + HALF_GRID_CELL):
                    kill_enemy(obj2)
    if obj.death_timer is not None:
        obj.death_timer -= 1
        if obj.death_timer <= 0:
            obj.obj_type = ObjType.World
            obj.collides = False
            obj.name = "Dead Enemy"
            obj.draw_priority = 2
            obj.sprite = obj.sprite[-1]

def update_enemy_flying(obj: Obj, destroy_list: List[Obj]):
    update_enemy_common(obj, destroy_list)


def update_enemy_walking(obj: Obj, destroy_list: List[Obj]):
    update_enemy_common(obj, destroy_list)

