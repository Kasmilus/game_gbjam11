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


def player_death():
    game.game.return_to_game = False
    game.game.game_state = game.GameState.GameOver
    game.game.time_since_game_over = 0
    game.game.player_pos_at_death = game.game.player_obj.get_pos()
    # TODO: One shot anim
    game.game.player_obj.sprite = resources.SPRITE_PLAYER_DEATH
    game.game.player_obj.player_speed = resources.SPRITE_PLAYER_DEATH_SPEED

    game.game.objects.append(Obj(pos=game.game.player_obj.get_pos(), **resources.ALL_OBJECTS['PARTICLE_EXPLOSION']))

    resources.play_sound(resources.SOUND_GAME_OVER, 0)
    resources.playm(1)

    game.game.cam_shake_timer = 0.7
    game.stop_frames = 30
    resources.flip_colors()


def update_player(obj: Obj, destroy_list: List[Obj]) -> None:
    player_current_room = get_room_from_pos((obj.pos_x, obj.pos_y))
    if get_current_room() != player_current_room:
        move_camera_to_new_room(player_current_room)

    # Check for dash (before hook test!)
    if obj.player_dash_timer <= 0.0:
        obj.player_speed = PLAYER_SPEED_NORMAL
        if Controls.b(one=True):
            obj.started_roll_hooked = obj.is_hooked
            obj.player_dash_timer = PLAYER_DASH_TIME
            obj.player_speed = PLAYER_SPEED_DASH
            if Controls.any_dir():
                resources.play_sound(resources.SOUND_ROLL)
    else:
        obj.player_dash_timer -= FRAME_TIME

    # Don't allow control when hooked
    if obj.is_hooked:
        obj.sprite = resources.SPRITE_PLAYER_ROLL
        obj.anim_speed = resources.SPRITE_PLAYER_ROLL_SPEED
        return

    # Check if fell into water
    for obj2 in game.game.objects:
        if obj2.obj_type is ObjType.Water:
            if game_object.collision_obj(obj, obj2):
                player_death()
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
    for obj2 in game.game.objects:
        if obj2 is not obj and obj2.obj_type is not ObjType.PlayerHook:
            move_dir = game_object.check_obj_move_collision(obj, obj2, move_dir)

    if move_dir[0] != 0 and move_dir[1] != 0:
        move_dir = move_dir[0] / 1.414, move_dir[1] / 1.414  # Normalize

    # Update position
    obj.pos_x += move_dir[0]
    obj.pos_y += move_dir[1]
    if move_dir != (0, 0):
        if move_dir[0] != 0 and move_dir[1] != 0:
            obj.last_move_dir = move_dir[0], 0
        else:
            obj.last_move_dir = move_dir
        if move_dir[0] != 0:
            obj.last_facing_dir_anim = move_dir[0]

        # Running particle
        if (Controls.left(one=True) or Controls.right(one=True)) and obj.player_particle_count < 2:
            run_particle = Obj(pos=obj.get_pos(), **resources.ALL_OBJECTS['PARTICLE_RUN'])
            if obj.last_facing_dir_anim < 0:
                run_particle.particle_invert = True
            game.game.objects.append(run_particle)
            obj.player_particle_count += 1

    # Hook shot
    if Controls.a(one=True):
        if obj.player_available_hooks > 0:
            obj.player_available_hooks -= 1
            start_pos_offset = 3
            hook_pos = (obj.pos_x + obj.last_move_dir[0] * start_pos_offset, obj.pos_y + obj.last_move_dir[1] * start_pos_offset)
            hook = Obj(**resources.ALL_OBJECTS['HOOK'], pos=hook_pos)
            hook.hook_velocity = (obj.last_move_dir[0] * obj.player_hook_speed, obj.last_move_dir[1] * obj.player_hook_speed)
            hook.hook_move_back_speed = obj.player_hook_speed*0.62
            game.game.objects.append(hook)
            resources.play_sound(resources.SOUND_HOOK_THROW)

    if Controls.any_dir(one=True):
        obj.last_input_frame = pyxel.frame_count
        obj.anim_speed = resources.SPRITE_PLAYER_RUN_SPEED
    if Controls.any_dir():
        obj.sprite = resources.SPRITE_PLAYER_RUN
        if obj.player_dash_timer > 0:
            obj.sprite = resources.SPRITE_PLAYER_ROLL
            obj.anim_speed = resources.SPRITE_PLAYER_ROLL_SPEED
    else:
        obj.sprite = resources.SPRITE_PLAYER_IDLE
        obj.anim_speed = resources.SPRITE_PLAYER_IDLE_SPEED


def draw_player(obj: Obj) -> None:
    invert = False
    if obj.last_facing_dir_anim < 0:
        invert = True

    render_sprite = obj.get_render_sprite()
    resources.blt_sprite(render_sprite, obj.pos_x, obj.pos_y, invert=invert)
