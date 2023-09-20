import math
from typing import List, Tuple
from enum import Enum
from copy import deepcopy

import pyxel

from constants import *
from room import *
import room_layouts
import utils
import interp
from controls import Controls
import resources
import game_object
import game
import obj_hook
import obj_player
import obj_enemy

# pyxel run main.py
# pyxel edit
# pyxel package . main.py
# pyxel app2html Pyxel.pyxapp
# pyxel app2exe Pyxel.pyxapp


def init():
    pyxel.init(160, 144, title="The Fable of Helga", fps=FPS, display_scale=3)
    pyxel.load("assets/my_resource.pyxres", image=True, tilemap=False, sound=True, music=True)

    game.init_game()

    # Start with player to make sure it's updated before anything else
    player_obj = Obj(pos=get_pos_for_room(cell_pos=(5, 5)), **resources.ALL_OBJECTS['PLAYER'])
    game.game.objects.append(player_obj)
    game.game.player_obj = player_obj

    # Rooms
    for level in room_layouts.ALL_LEVELS:
        room_name = level[0]
        room_pos = level[1]
        layouts = level[2]
        for layout in layouts:
            create_room(layout, room_pos, room_name)

    #create_room(room_layouts.ROOM_LAYOUT_TEST, (0, 0))
    #create_room(room_layouts.ROOM_DECOR_TEST, (0, 0))
    #create_room(room_layouts.ROOM_LAYOUT_TEST, (1, 0))

    resources.play_music(resources.MUSIC_A)

    global game_checkpoint
    game_checkpoint = deepcopy(game.game)


def update():
    global game
    global game_checkpoint

    if game.game.stop_frames > 0:
        return
    #
    # Update camera
    #
    if game.game.camera_x != game.game.camera_target_x or game.game.camera_y != game.game.camera_target_y:
        CAMERA_MOVE_TIME = 1
        game.game.camera_x = interp.interp(game.game.camera_x, game.game.camera_target_x, game.game.camera_move_timer, CAMERA_MOVE_TIME, interp.EasingType.Slerp)
        game.game.camera_y = interp.interp(game.game.camera_y, game.game.camera_target_y, game.game.camera_move_timer, CAMERA_MOVE_TIME, interp.EasingType.Slerp)
        game.game.camera_move_timer += FRAME_TIME
        pyxel.camera(game.game.camera_x, game.game.camera_y)
        return  # Don#t update anythin when moving camera

    #if pyxel.btn(pyxel.KEY_Q):
        #pyxel.quit()
    if game.game.game_state == game.GameState.Splash:
        game.game.splash_timer += FRAME_TIME
        if game.game.splash_timer > 1.5:
            game.game.game_state = game.GameState.PressToStart
    elif game.game.game_state == game.GameState.PressToStart:
        game.game.press_to_start_timer += FRAME_TIME
        if Controls.any():
            game.game.game_state = game.GameState.Game
        if game.game.press_to_start_timer > 1.2:
            game.game.press_to_start_timer = 0
    elif game.game.game_state == game.GameState.GameOver:
        game.game.time_since_game_over += FRAME_TIME
        if game.game.return_to_game:
            if game.game.time_since_game_over > GAME_RESTART_TIME:
                #del game.game.player_obj
                #del game.game
                game.game = game_checkpoint
                game.game.game_state = game.GameState.Game
        elif game.game.time_since_game_over > 1.5 and Controls.any():
                game.game.return_to_game = True
                game.game.time_since_game_over = 0
    else:
        #
        # Game Logic updates
        #
        destroy_list = []
        for obj_idx, obj in enumerate(game.game.objects):
            if obj.is_pushable:
                for obj2 in game.game.objects:
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
                            #if move_dir:
                            #    obj.pos_x += move_dir[0]
                            #    obj.pos_y += move_dir[1]
            if obj.obj_type == ObjType.PlayerHook:
                obj_hook.update_hook(obj, destroy_list)
            elif obj.obj_type == ObjType.Player:
                obj_player.update_player(obj, destroy_list)
            elif obj.obj_type == ObjType.EnemyFlying:
                obj_enemy.update_enemy_flying(obj, destroy_list)
            elif obj.obj_type == ObjType.EnemyWalking:
                obj_enemy.update_enemy_flying(obj, destroy_list)
            elif obj.obj_type == ObjType.Coin:
                if game_object.get_dist_obj(obj, game.game.player_obj) < GRID_CELL_SIZE:
                    game.game.player_obj.player_collected_coins += 1
                    destroy_list.append(obj)
            elif obj.obj_type == ObjType.Key:
                if game_object.get_dist_obj(obj, game.game.player_obj) < GRID_CELL_SIZE:
                    game.game.player_obj.player_collected_keys += 1
                    destroy_list.append(obj)
            elif obj.obj_type == ObjType.Door:
                if game_object.get_dist_obj(obj, game.game.player_obj) < GRID_CELL_SIZE:
                    if game.game.player_obj.player_collected_keys > 0:
                        game.game.player_obj.player_collected_keys -= 1
                        destroy_list.append(obj)
            elif obj.obj_type == ObjType.Checkpoint:
                if not obj.checkpoint_used:
                    if game_object.get_dist_obj(obj, game.game.player_obj) < GRID_CELL_SIZE + HALF_GRID_CELL:
                        obj.checkpoint_used = True
                        obj.last_input_frame = pyxel.frame_count
                        game.game.player_obj.player_last_checkpoint_name = obj.checkpoint_name
                        # Save game state
                        game_checkpoint = deepcopy(game.game)
            elif obj.obj_type == ObjType.ParticleRun or obj.obj_type == ObjType.ParticleExplosion:
                obj.particle_lifetime -= 1
                if obj.particle_lifetime <= 1:
                    destroy_list.append(obj)
                    game.game.player_obj.player_particle_count -= 1

            if obj.velocity is not None and obj.velocity != (0, 0):
                vel_sign_x = utils.sign(obj.velocity[0])
                vel_sign_y = utils.sign(obj.velocity[1])
                for obj2 in game.game.objects:
                    if obj2 is not obj and obj2.obj_type is not ObjType.PlayerHook:
                        move_dir = game_object.check_obj_move_collision(obj, obj2, (vel_sign_x, vel_sign_y))
                        if move_dir[0] != vel_sign_x or move_dir[1] != vel_sign_y:
                            obj.velocity = (0, 0)
                            obj.collided_during_hook = True
                obj.pos_x += obj.velocity[0] * FRAME_TIME
                obj.pos_y += obj.velocity[1] * FRAME_TIME
                obj.velocity = (obj.velocity[0] - utils.sign(obj.velocity[0]) * obj.velocity_drag,
                                obj.velocity[1] - utils.sign(obj.velocity[1]) * obj.velocity_drag)
                if abs(obj.velocity[0]) < 8:
                    obj.velocity = 0, obj.velocity[1]
                if abs(obj.velocity[1]) < 8:
                    obj.velocity = obj.velocity[0], 0

        #
        # Frame state reset
        #
        for obj in destroy_list:
            game.game.objects.remove(obj)
        for obj in game.game.objects:
            obj.collisions = []


def draw():
    if game.game.stop_frames > 0:
        game.game.stop_frames -= 1
        return

    pyxel.cls(resources.COLOR_BACKGROUND)
    if game.game.game_state == game.GameState.Splash:
        if game.game.splash_timer <= 1:
            y_pos = interp.interp(-144, 0, game.game.splash_timer, 1.0, easing=interp.EasingType.EaseOutBounce)
        else:
            y_pos = 0
        resources.blt_splash(0, y_pos)
    elif game.game.game_state == game.GameState.PressToStart:
        resources.blt_splash(0, 0)
        if game.game.press_to_start_timer < 0.8:
            pyxel.rect(25, 115, 110, 15, resources.COLOR_BACKGROUND)
            pyxel.rectb(25, 115, 110, 15, resources.COLOR_DARK)
            pyxel.text(31, 121, "PRESS ANY BUTTON TO START", resources.COLOR_DARK)
    elif game.game.game_state == game.GameState.GameOver:
        if not game.game.return_to_game:
            if game.game.time_since_game_over > GAME_DEATH_TIME:
                pyxel.text(game.game.camera_x + 31, game.game.camera_y + 121, "PRESS ANY BUTTON TO START", resources.COLOR_DARK)
            elif pyxel.frame_count % 4 == 0:
                resources.flip_colors()
        else:
            game.game.player_obj.pos_x = interp.interp(game.game.player_pos_at_death[0], game_checkpoint.player_obj.pos_x, game.game.time_since_game_over, GAME_RESTART_TIME, interp.EasingType.EaseOutCubic)
            game.game.player_obj.pos_y = interp.interp(game.game.player_pos_at_death[1], game_checkpoint.player_obj.pos_y, game.game.time_since_game_over, GAME_RESTART_TIME, interp.EasingType.EaseOutCubic)
        resources.blt_sprite(game.game.player_obj.sprite[-1], game.game.player_obj.pos_x, game.game.player_obj.pos_y, invert=game.game.player_obj.last_facing_dir_anim < 0)
        resources.reset_color()
    elif game.game.game_state == game.GameState.Game:
        #
        # Sort draw list
        #
        draw_list = []
        for obj in game.game.objects:
            draw_list.append(obj)
        draw_list.sort(key=lambda x: x.draw_priority)

        #
        # Render
        #
        for obj in draw_list:
            if obj.obj_type == ObjType.PlayerHook:
                obj_hook.draw_hook(obj)
            elif obj.obj_type == ObjType.Player:
                obj_player.draw_player(obj)
            elif obj.obj_type == ObjType.Checkpoint:
                # Fire anim once only!
                if obj.checkpoint_used is False:
                    resources.blt_sprite(obj.sprite[0], obj.pos_x, obj.pos_y)
                elif (pyxel.frame_count - obj.last_input_frame) >= (obj.anim_speed * len(obj.sprite)):
                    resources.blt_sprite(obj.sprite[-1], obj.pos_x, obj.pos_y)
                else:
                    resources.blt_sprite(obj.get_render_sprite(), obj.pos_x, obj.pos_y)
            else:
                invert = False
                invert_y = False
                if obj.obj_type == ObjType.ParticleRun or obj.obj_type == ObjType.ParticleExplosion:
                    invert = obj.particle_invert
                    invert_y = obj.particle_invert_y
                resources.blt_sprite(obj.get_render_sprite(), obj.pos_x, obj.pos_y, invert=invert, invert_y=invert_y)

            if DEBUG_DRAW_COLLIDERS:
                if obj.collides:
                    bbox = obj.get_bbox_world_space()
                    pyxel.rectb(bbox[0], bbox[1], bbox[2]-bbox[0], bbox[3]-bbox[1], 15)

        # Draw UI
        pos_x = game.game.camera_x
        pos_y = game.game.camera_y + ROOM_SIZE_Y*GRID_CELL_SIZE
        resources.blt_ui_sprite(resources.SPRITE_UI_BOX, (GRID_CELL_SIZE*ROOM_SIZE_X, GRID_CELL_SIZE*2), pos_x, pos_y )

        pos_y += HALF_GRID_CELL
        pos_x += HALF_GRID_CELL/2
        resources.blt_ui_sprite(resources.SPRITE_UI_HOOK, (GRID_CELL_SIZE*ROOM_SIZE_X, GRID_CELL_SIZE), pos_x, pos_y)

        pos_x += GRID_CELL_SIZE
        pyxel.text(pos_x-3, pos_y+5, f":{game.game.player_obj.player_available_hooks}", resources.COLOR_DARK)

        pos_x += HALF_GRID_CELL
        resources.blt_ui_sprite(resources.SPRITE_UI_KEY, (GRID_CELL_SIZE*ROOM_SIZE_X, GRID_CELL_SIZE), pos_x, pos_y-1)
        pos_x += GRID_CELL_SIZE
        pyxel.text(pos_x, pos_y+5, f":{game.game.player_obj.player_collected_keys}", resources.COLOR_DARK)

        pos_x += HALF_GRID_CELL
        resources.blt_ui_sprite(resources.SPRITE_UI_COIN, (GRID_CELL_SIZE*ROOM_SIZE_X, GRID_CELL_SIZE), pos_x, pos_y)
        pos_x += GRID_CELL_SIZE
        pyxel.text(pos_x-3, pos_y+5, f":{game.game.player_obj.player_collected_coins}", resources.COLOR_DARK)

        pos_x += GRID_CELL_SIZE
        resources.blt_ui_sprite(resources.SPRITE_UI_CKPT, (GRID_CELL_SIZE*ROOM_SIZE_X, GRID_CELL_SIZE), pos_x, pos_y)
        #pos_x += GRID_CELL_SIZE + HALF_GRID_CELL + 1
        pos_x += GRID_CELL_SIZE
        #s = "1234567891234"
        s = game.game.player_obj.player_last_checkpoint_name
        # Center the text
        pos_x += (13-len(s)) * 2  # Each char is 4 pixels wide (3 + spacing)
        pyxel.text(pos_x, pos_y+6, s, resources.COLOR_DARK)


init()
pyxel.run(update, draw)
