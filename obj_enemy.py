import math
from typing import List, Tuple
from enum import Enum

import pyxel

import obj_player
from constants import *
from room import *
import room_layouts
import utils
import interp
from controls import Controls
import resources
import game_object
from game import *


def kill_enemy(obj: Obj):
    game.game.objects.append(Obj(pos=obj.get_pos(), **resources.ALL_OBJECTS['PARTICLE_EXPLOSION']))
    if obj.obj_type is ObjType.EnemyFlying:
        obj.sprite = resources.SPRITE_ENEMY_FLYING_DEATH
        obj.anim_speed = resources.SPRITE_ENEMY_FLYING_DEATH_SPEED + pyxel.rndi(0, 2)
    elif obj.obj_type is ObjType.EnemyWalking:
        obj.sprite = resources.SPRITE_ENEMY_WALKING_DEATH
        obj.anim_speed = resources.SPRITE_ENEMY_WALKING_DEATH_SPEED + pyxel.rndi(0, 2)
    obj.death_timer = obj.anim_speed * len(obj.sprite)
    game.stop_frames = 3

    if game_object.get_dist_obj(obj, game.game.player_obj) < GRID_CELL_SIZE:
        obj_player.player_death()

    if pyxel.rndi(0, 1) == 0:
        resources.play_sound(resources.SOUND_ENEMY_DEATH_A)
    else:
        resources.play_sound(resources.SOUND_ENEMY_DEATH_B)


def update_enemy_common(obj: Obj, destroy_list: List[Obj]):
    if game_object.collision_obj(obj, game.game.player_obj):
        obj_player.player_death()

    if obj.collided_during_hook is True and obj.death_timer is None:
        # Initiate death anim
        kill_enemy(obj)
        for obj2 in game.game.objects:
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

    # Check if should move
    d = (game.game.player_obj.pos_x - obj.pos_x, game.game.player_obj.pos_y - obj.pos_y)
    dist_to_player = utils.get_vector_len(d)
    if dist_to_player < ENEMY_CHASE_DIST:
        move = True
        for obj2 in game.game.objects:
            if obj is obj2 or obj2.obj_type in [ObjType.Player, ObjType.PlayerHook] or obj2.collides is False:
                continue
            result = game_object.get_line_bb_intersection_point(obj.get_pos_mid(), game.game.player_obj.get_pos_mid(), obj.bounding_box)
            if result is not None:
                move = False
                break
        if move is True:
            d = utils.get_vector_normalised(d)
            for obj2 in game.game.objects:
                if obj is obj2 or obj2.obj_type in [ObjType.Player, ObjType.PlayerHook] or obj2.collides is False:
                    continue
                d = game_object.check_obj_move_collision(obj, obj2, d)
            obj.pos_x += d[0]*obj.enemy_speed
            obj.pos_y += d[1]*obj.enemy_speed

def update_enemy_flying(obj: Obj, destroy_list: List[Obj]):
    update_enemy_common(obj, destroy_list)


def update_enemy_walking(obj: Obj, destroy_list: List[Obj]):
    update_enemy_common(obj, destroy_list)

