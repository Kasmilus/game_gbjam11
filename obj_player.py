import math
from typing import List, Tuple
from enum import Enum

import pyxel

import game
import utils
from constants import *
from room import *
import room_layouts
from utils import *
import interp
from controls import Controls
import resources
import game_object
from game import *


def update_player(obj: Obj, destroy_list: List[Obj]) -> None:
    player_current_room = get_room_from_pos((obj.pos_x, obj.pos_y))
    if get_current_room() != player_current_room:
        move_camera_to_new_room(player_current_room)

    # Check for dash (before hook test!)
    if obj.player_dash_timer <= 0.0:
        obj.player_speed = 0.8
        if Controls.b(one=True):
            obj.player_dash_timer = 0.25
            obj.player_speed = 1.6
    else:
        obj.player_dash_timer -= FRAME_TIME

    # Don't allow control when hooked
    if obj.is_hooked:
        return

    # Check movement input dir
    move_dir = [0, 0]
    if Controls.down():
        move_dir[1] += obj.player_speed
    elif Controls.up():
        move_dir[1] -= obj.player_speed
    if Controls.left():
        move_dir[0] -= obj.player_speed
    elif Controls.right():
        move_dir[0] += obj.player_speed
    # Check if movement would result in collision
    for obj2 in game.objects:
        if obj2 is not obj and obj2.obj_type is not ObjType.PlayerHook:
            move_dir = game_object.check_obj_move_collision(obj, obj2, move_dir)
            #if game_object.collision_bb((obj.pos_x + move_dir[0], obj.pos_y), obj.bounding_box, obj2.get_pos(), obj2.bounding_box):
            #    move_dir[0] = 0
            #if game_object.collision_bb((obj.pos_x, obj.pos_y + move_dir[1]), obj.bounding_box, obj2.get_pos(), obj2.bounding_box):
            #    move_dir[1] = 0

    if move_dir[0] != 0 and move_dir[1] != 0:
        move_dir = move_dir[0] / 1.414, move_dir[1] / 1.414  # Normalize

    # Update position
    obj.pos_x += move_dir[0]
    obj.pos_y += move_dir[1]
    if move_dir != (0, 0):
        obj.last_move_dir = move_dir

    # Hook shot
    if Controls.a(one=True):
        if obj.player_available_hooks > 0:
            obj.player_available_hooks -= 1
            start_pos_offset = 3
            hook_pos = (obj.pos_x + obj.last_move_dir[0] * start_pos_offset, obj.pos_y + obj.last_move_dir[1] * start_pos_offset)
            hook = Obj(ObjType.PlayerHook, sprite=resources.SPRITE_HOOK, pos=hook_pos)
            hook.hook_velocity = (obj.last_move_dir[0] * obj.player_hook_speed, obj.last_move_dir[1] * obj.player_hook_speed)
            hook.hook_move_back_speed = obj.player_hook_speed
            game.objects.append(hook)

def draw_player(obj: Obj) -> None:
    resources.blt_sprite(obj.sprite, obj.pos_x, obj.pos_y)