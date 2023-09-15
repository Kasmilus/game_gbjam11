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
    game.objects.append(Obj(ObjType.Player, sprite=resources.SPRITE_PLAYER, pos=get_pos_for_room(cell_pos=(5, 5))))

    # Rooms
    create_room(room_layouts.ROOM_LAYOUT_TEST, (0, 0))
    create_room(room_layouts.ROOM_LAYOUT_TEST, (1, 0))
    game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_A, pos=get_pos_for_room((1, 5))))
    game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_B, pos=get_pos_for_room((2, 4))))

    game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_A, pos=get_pos_for_room((4, 5))))
    game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_B, pos=get_pos_for_room((6, 5))))

    # Enemies (spawn them on room enter if entering for the first time?)
    # TODO

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
        # Collision checks
        #
        for obj in game.objects:
            for obj2 in game.objects:
                if obj is not obj2 and game_object.collision_obj(obj, obj2):
                    obj.collisions.append(obj2)
        #
        # Game Logic updates
        #
        for obj in game.objects:
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
                    if obj2 is not obj:
                        #if game_object.collision_bb(pos_x=obj.pos_x+move_dir[0], pos_y=obj.pos_y, posb_x=obj2.pos_x, posb_y=obj2.pos_y, size=obj.bounding_box[2]-obj.bounding_box[0]):
                        if game_object.collision_bb((obj.pos_x + move_dir[0], obj.pos_y), obj.bounding_box, obj2.get_pos(), obj2.bounding_box):
                            move_dir[0] = 0
                        if game_object.collision_bb((obj.pos_x, obj.pos_y + move_dir[1]), obj.bounding_box, obj2.get_pos(), obj2.bounding_box):
                        #if collision(pos_x=obj.pos_x, pos_y=obj.pos_y+move_dir[1], posb_x=obj2.pos_x, posb_y=obj2.pos_y, size=obj.bounding_box[3]-obj.bounding_box[1]):
                            move_dir[1] = 0

                if move_dir[0] != 0 and move_dir[1] != 0:
                    move_dir[0] /= 1.414  # Normalize
                    move_dir[1] /= 1.414  # Normalize

                # Update position
                room_before_move = get_room_from_pos((obj.pos_x, obj.pos_y))
                obj.pos_x += move_dir[0]
                obj.pos_y += move_dir[1]

                room_after_move = get_room_from_pos((obj.pos_x, obj.pos_y))
                if room_after_move != room_before_move:
                    move_camera_to_new_room(room_after_move)
        #
        # Frame state reset
        #
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

        #
        # Render
        #
        for obj in draw_list:
            resources.blt_sprite(obj.sprite, obj.pos_x, obj.pos_y)



init()
pyxel.run(update, draw)
