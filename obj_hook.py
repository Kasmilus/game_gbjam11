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


def update_hook(obj: Obj, destroy_list: List[Obj]) -> None:
    destroy_hook = False

    if Controls.b(one=True) and Controls.any_dir(one=False):
        destroy_hook = True
    # First check if line collides
    for obj2 in game.objects:
        if obj2.obj_type == ObjType.PlayerHook or obj2.obj_type == ObjType.Water or obj2.collides is False:
            continue
        if obj2.obj_type == ObjType.Player and obj.hook_attached_object is not None:
            if game_object.get_dist_obj(obj, obj2) < 3:
                destroy_hook = True
                break
        b_box = obj2.get_bbox_world_space()
        # TODO: Should allow "wrapping" the line around an object... count to 2 secs and destroy if still in contact
        if game_object.get_line_bb_intersection_point(obj.get_hook_attach_point(game), game.player_obj.get_pos_mid(), b_box):
            if obj2.obj_type == ObjType.Player:
                continue
            destroy_hook = True
            break
    # Move hook before attached
    if obj.hook_attached_object is None:
        assert obj.hook_velocity is not None
        obj.pos_x += obj.hook_velocity[0] * FRAME_TIME
        obj.pos_y += obj.hook_velocity[1] * FRAME_TIME
        hook_drag = obj.hook_drag * FRAME_TIME

        # TODO: Never allow it to go below certain speed?
        obj.hook_velocity = (obj.hook_velocity[0] - sign(obj.hook_velocity[0]) * hook_drag,
                             obj.hook_velocity[1] - sign(obj.hook_velocity[1]) * hook_drag)
        for obj2 in game.objects:
            if obj2.obj_type in [ObjType.Player, ObjType.Water] or obj2 is obj or not game_object.objs_can_collide(obj, obj2):
                continue
            if game_object.collision_obj(obj, obj2):
                # TODO: Anim slow down before coming back
                if obj2.is_hookable:
                    obj.hook_attached_object = obj2
                else:
                    obj.hook_attached_object = game.player_obj
                obj.hook_attached_object.is_hooked = True
    else:
        # already attached, move back
        if obj.hook_move_back_speed > 48:
            obj.hook_move_back_speed -= 10 * FRAME_TIME
        hook_move_dir = (game.player_obj.pos_x - obj.pos_x,
                         game.player_obj.pos_y - obj.pos_y)
        hook_move_dir = get_vector_normalised(hook_move_dir)
        move_vector = hook_move_dir[0] * obj.hook_move_back_speed * FRAME_TIME, hook_move_dir[1] * obj.hook_move_back_speed * FRAME_TIME
        if obj.hook_attached_object is game.player_obj:
            move_vector = -move_vector[0], -move_vector[1]
        else:
            obj.pos_x += move_vector[0]
            obj.pos_y += move_vector[1]
        update_hooked_obj = True
        for obj2 in game.objects:
            if obj2 is obj or obj2 is obj.hook_attached_object or obj2.obj_type is ObjType.Water or not game_object.objs_can_collide(obj.hook_attached_object, obj2):
                continue
            if game_object.collision_bb((obj.hook_attached_object.pos_x + move_vector[0], obj.hook_attached_object.pos_y + move_vector[1]), obj.hook_attached_object.bounding_box,
                                        obj2.get_pos(), obj2.bounding_box):
                update_hooked_obj = False
                destroy_hook = True
                break
        if update_hooked_obj:
            obj.hook_attached_object.pos_x += move_vector[0]
            obj.hook_attached_object.pos_y += move_vector[1]

    if destroy_hook:
        if obj.hook_attached_object is not None:
            obj.hook_attached_object.is_hooked = False
            if obj.hook_attached_object.obj_type is not ObjType.Player:
                assert move_vector is not None
                obj.hook_attached_object.velocity = move_vector[0] * obj.hook_move_back_speed, move_vector[1] * obj.hook_move_back_speed
        game.player_obj.player_available_hooks += 1
        assert game.player_obj.player_available_hooks <= game.player_obj.player_max_hooks
        destroy_list.append(obj)

def draw_hook(obj: Obj) -> None:
    hook_point = obj.get_hook_attach_point(game)
    pyxel.line(hook_point[0], hook_point[1],
               game.player_obj.pos_x + HALF_GRID_CELL, game.player_obj.pos_y + HALF_GRID_CELL,
               resources.COLOR_DARK)
    resources.blt_sprite(obj.get_render_sprite(), obj.pos_x, obj.pos_y)
