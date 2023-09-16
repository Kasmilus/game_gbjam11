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

# pyxel run main.py
# pyxel edit
# pyxel package . main.py
# pyxel app2html Pyxel.pyxapp
# pyxel app2exe Pyxel.pyxapp


def init():
    pyxel.init(160, 144, title="Game Name", fps=FPS, display_scale=3)
    pyxel.load("assets/my_resource.pyxres", image=True, tilemap=False, sound=True, music=True)

    # Start with player to make sure it's updated before anything else
    player_obj = Obj(ObjType.Player, sprite=resources.SPRITE_PLAYER, pos=get_pos_for_room(cell_pos=(5, 5)))
    game.objects.append(player_obj)
    game.player_obj = player_obj

    # Rooms
    create_room(room_layouts.ROOM_LAYOUT_TEST, (0, 0))
    create_room(room_layouts.ROOM_LAYOUT_TEST, (1, 0))
    game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_A, pos=get_pos_for_room((1, 5))))
    game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_B, pos=get_pos_for_room((2, 4))))

    game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_A, pos=get_pos_for_room((4, 5))))
    game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_B, pos=get_pos_for_room((6, 5)), is_hookable=True))

    # Enemies (spawn them on room enter if entering for the first time?)
    game.objects.append(Obj(ObjType.Enemy, sprite=resources.SPRITE_ENEMY_A, pos=get_pos_for_room((5, 3)), is_hookable=True))

    resources.play_music(resources.MUSIC_A)


def update():
    #
    # Update camera
    #
    if game.camera_x != game.camera_target_x or game.camera_y != game.camera_target_y:
        CAMERA_MOVE_TIME = 1
        game.camera_x = interp.interp(game.camera_x, game.camera_target_x, game.camera_move_timer, CAMERA_MOVE_TIME, interp.EasingType.Slerp)
        game.camera_y = interp.interp(game.camera_y, game.camera_target_y, game.camera_move_timer, CAMERA_MOVE_TIME, interp.EasingType.Slerp)
        game.camera_move_timer += FRAME_TIME
        pyxel.camera(game.camera_x, game.camera_y)
        return  # Don#t update anythin when moving camera

    #if pyxel.btn(pyxel.KEY_Q):
        #pyxel.quit()
    if game.game_state == GameState.Splash:
        game.splash_timer += FRAME_TIME
        if game.splash_timer > 1.5:
            game.game_state = GameState.PressToStart
    elif game.game_state == GameState.PressToStart:
        game.press_to_start_timer += FRAME_TIME
        if Controls.any():
            game.game_state = GameState.Game
        if game.press_to_start_timer > 1.2:
            game.press_to_start_timer = 0
    else:
        #
        # Game Logic updates
        #
        destroy_list = []
        for obj_idx, obj in enumerate(game.objects):
            if obj.obj_type == ObjType.PlayerHook:
                destroy_hook = False
                # First check if line collides
                for obj2 in game.objects:
                    if obj2.obj_type == ObjType.PlayerHook:
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
                        if obj2.obj_type is ObjType.Player or obj2 is obj:
                            continue
                        if game_object.collision_obj(obj, obj2):
                            # TODO: Anim slow down before coming back
                            if obj2.is_hookable:
                                obj.hook_attached_object = obj2
                            else:
                                obj.hook_attached_object = game.player_obj
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
                        if obj2 is obj or obj2 is obj.hook_attached_object:
                            continue
                        if game_object.collision_bb((obj.hook_attached_object.pos_x + move_vector[0], obj.hook_attached_object.pos_y + move_vector[1]), obj.hook_attached_object.bounding_box, obj2.get_pos(), obj2.bounding_box):
                            update_hooked_obj = False
                            destroy_hook = True
                            break
                    if update_hooked_obj:
                        obj.hook_attached_object.pos_x += move_vector[0]
                        obj.hook_attached_object.pos_y += move_vector[1]
                if destroy_hook:
                    game.player_obj.player_available_hooks += 1
                    assert game.player_obj.player_available_hooks <= game.player_obj.player_max_hooks
                    destroy_list.append(obj_idx)

            if obj.is_pushable:
                for obj2 in game.objects:
                    if obj2 is not obj and obj2.obj_type is not ObjType.PlayerHook:
                        if game_object.collision_obj(obj, obj2):
                            # Collides! check if we can free ourselves by moving 1 or 2 pixels in any way
                            move_dir = None
                            for i in [1, 2]:
                                if move_dir is not None:
                                    break
                                for dir in [(i, 0), (0, i), (-i, 0), (0, -i)]:
                                    if not game_object.collision_bb((obj.pos_x + dir[0], obj.pos_y + dir[1]), obj.bounding_box, obj2.get_pos(), obj2.bounding_box):
                                        move_dir = dir
                                        break
                            if move_dir:
                                obj.pos_x += move_dir[0]
                                obj.pos_y += move_dir[1]
            if obj.obj_type == ObjType.Player:
                if obj.player_dash_timer <= 0.0:
                    obj.player_speed = 0.8
                    if Controls.b(one=True):
                        obj.player_dash_timer = 0.25
                        obj.player_speed = 1.6
                else:
                    obj.player_dash_timer -= FRAME_TIME

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
                        if game_object.collision_bb((obj.pos_x + move_dir[0], obj.pos_y), obj.bounding_box, obj2.get_pos(), obj2.bounding_box):
                            move_dir[0] = 0
                        if game_object.collision_bb((obj.pos_x, obj.pos_y + move_dir[1]), obj.bounding_box, obj2.get_pos(), obj2.bounding_box):
                            move_dir[1] = 0

                if move_dir[0] != 0 and move_dir[1] != 0:
                    move_dir[0] /= 1.414  # Normalize
                    move_dir[1] /= 1.414  # Normalize

                # Update position
                room_before_move = get_room_from_pos((obj.pos_x, obj.pos_y))
                obj.pos_x += move_dir[0]
                obj.pos_y += move_dir[1]
                if move_dir != [0, 0]:
                    obj.last_move_dir = move_dir

                room_after_move = get_room_from_pos((obj.pos_x, obj.pos_y))
                if room_after_move != room_before_move:
                    move_camera_to_new_room(room_after_move)

                # Hook shot
                if Controls.a(one=True):
                    if obj.player_available_hooks > 0:
                        obj.player_available_hooks -= 1
                        start_pos_offset = 3
                        hook_pos = (obj.pos_x + obj.last_move_dir[0]*start_pos_offset, obj.pos_y + obj.last_move_dir[1]*start_pos_offset)
                        hook = Obj(ObjType.PlayerHook, sprite=resources.SPRITE_HOOK, pos=hook_pos)
                        hook.hook_velocity = (obj.last_move_dir[0] * obj.player_hook_speed, obj.last_move_dir[1] * obj.player_hook_speed)
                        hook.hook_move_back_speed = obj.player_hook_speed
                        game.objects.append(hook)
        #
        # Frame state reset
        #
        for id in destroy_list:
            game.objects.pop(id)
        for obj in game.objects:
            obj.collisions = []



def draw():
    pyxel.cls(resources.COLOR_BACKGROUND)
    if game.game_state == GameState.Splash:
        if game.splash_timer <= 1:
            y_pos = interp.interp(-144, 0, game.splash_timer, 1.0, easing=interp.EasingType.EaseOutBounce)
        else:
            y_pos = 0
        resources.blt_splash(0, y_pos)
    elif game.game_state == GameState.PressToStart:
        resources.blt_splash(0, 0)
        if game.press_to_start_timer < 0.8:
            pyxel.rect(25, 115, 110, 15, resources.COLOR_BACKGROUND)
            pyxel.rectb(25, 115, 110, 15, resources.COLOR_DARK)
            pyxel.text(31, 121, "PRESS ANY BUTTON TO START", resources.COLOR_DARK)
    elif game.game_state == GameState.Game:
        #
        # Sort draw list
        #
        draw_list = []
        for obj in game.objects:
            draw_list.append(obj)
        draw_list.sort(key=lambda x: x.draw_priority)

        #pyxel.line(game.test_x, game.test_y, pyxel.mouse_x, pyxel.mouse_y, resources.COLOR_DARK)
        #pyxel.line(game.test_x_start, game.test_y_start, game.test_x_end, game.test_x_end, resources.COLOR_DARK)
        #point = game_object.get_line_intersection_point((game.test_x, game.test_y), (pyxel.mouse_x, pyxel.mouse_y),
                                                   #(game.test_x_start, game.test_y_start), (game.test_x_end, game.test_x_end))
        #if point is not None:
            #pyxel.circ(point[0], point[1], 3, resources.COLOR_DARK)

        #
        # Render
        #
        for obj in draw_list:
            resources.blt_sprite(obj.sprite, obj.pos_x, obj.pos_y)
            if obj.obj_type == ObjType.PlayerHook:
                hook_point = obj.get_hook_attach_point(game)
                pyxel.line(hook_point[0], hook_point[1],
                           game.player_obj.pos_x + HALF_GRID_CELL, game.player_obj.pos_y + HALF_GRID_CELL,
                           resources.COLOR_DARK)


init()
pyxel.run(update, draw)
