import math
from typing import List, Tuple, TypedDict
from enum import Enum

import pyxel

from utils import *
import interp
from controls import Controls
import resources

# pyxel run main.py
# pyxel edit
# pyxel package . main.py
# pyxel app2html Pyxel.pyxapp
# pyxel app2exe Pyxel.pyxapp

FPS: int = 60
FRAME_TIME: float = 1/FPS
GRID_CELL_SIZE: int = 16
ROOM_SIZE_X: int = 10
ROOM_SIZE_Y: int = 9

class GameState(Enum):
    Splash = 1,
    PressToStart = 2,
    Game = 3

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

class Game:
    game_state: GameState = GameState.Game
    #game_state: GameState = GameState.Splash
    objects: List[Obj] = []

    splash_timer: float = 0
    press_to_start_timer: float = 0

    camera_x: int = 0
    camera_y: int = 0
    camera_target_x: int = 0
    camera_target_y: int = 0
    camera_move_timer: float = 0

    def move_camera_to_new_room(self, room_coords: Tuple[int, int]) -> None:
        self.camera_target_x, self.camera_target_y = get_pos_from_room_coords(room_coords)
        self.camera_move_timer = 0


game: Game = Game()


def get_pos_for_room(cell_pos: Tuple[int, int], room_coords: Tuple[int, int] = None) -> Tuple[int, int]:
    if room_coords is None:
        room_coords = (0, 0)  # TODO: get current room
    room_origin = get_pos_from_room_coords(room_coords)
    return room_origin[0] + cell_pos[0] * GRID_CELL_SIZE, room_origin[1] + cell_pos[1] * GRID_CELL_SIZE


def create_room(layout: str, room_coords: Tuple[int, int]) -> None:
    lines = layout.splitlines()
    assert len(lines) == ROOM_SIZE_Y
    for cell_pos_y, line in enumerate(lines):
        assert len(line) == ROOM_SIZE_X
        for cell_pos_x, c in enumerate(line):
            if c == '0':
                continue
            elif c == '1':
                game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_A, pos=get_pos_for_room(cell_pos=(cell_pos_x, cell_pos_y), room_coords=room_coords)))
            elif c == '2':
                game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_B, pos=get_pos_for_room(cell_pos=(cell_pos_x, cell_pos_y), room_coords=room_coords)))
            else:
                raise Exception("Unknown cell type!")

def get_room_from_pos(pos: Tuple[int, int]) -> Tuple[int, int]:
    cell_coord = round(pos[0] / GRID_CELL_SIZE), round(pos[1] / GRID_CELL_SIZE)
    room_coord = math.floor(cell_coord[0] / ROOM_SIZE_X), math.floor(cell_coord[1] / ROOM_SIZE_Y)
    return room_coord

def get_pos_from_room_coords(room_coords: Tuple[int, int]) -> Tuple[int, int]:
    pos = room_coords[0] * ROOM_SIZE_X * GRID_CELL_SIZE, room_coords[1] * ROOM_SIZE_Y * GRID_CELL_SIZE
    return pos

def init():
    pyxel.init(160, 144, title="Game Name", fps=FPS, display_scale=3)
    pyxel.load("assets/my_resource.pyxres", image=True, tilemap=False, sound=True, music=True)

    # Start with player to make sure it's updated before anything else
    game.objects.append(Obj(ObjType.Player, sprite=resources.SPRITE_PLAYER, pos=get_pos_for_room(cell_pos=(5, 5))))

    # Rooms
    test_layout = "1111111111\n" \
                  "1000000001\n" \
                  "1000000001\n" \
                  "1000000001\n" \
                  "0000000000\n" \
                  "1000000001\n" \
                  "2000000001\n" \
                  "2000000001\n" \
                  "1112011111"
    create_room(test_layout, (0, 0))
    create_room(test_layout, (1, 0))
    game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_A, pos=get_pos_for_room((1, 5))))
    game.objects.append(Obj(ObjType.World, sprite=resources.SPRITE_WALL_B, pos=get_pos_for_room((2, 4))))

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
                if obj is not obj2 and collision(obj.pos_x, obj.pos_y, obj2.pos_x, obj2.pos_y):
                    obj.collisions.append(obj2)
        #
        # Game Logic updates
        #
        for obj in game.objects:
            if obj.obj_type == ObjType.Player:
                room_before_move = get_room_from_pos((obj.pos_x, obj.pos_y))
                player_speed = 0.8
                if Controls.down():
                    obj.pos_y += player_speed
                if Controls.up():
                    obj.pos_y -= player_speed
                if Controls.left():
                    obj.pos_x -= player_speed
                if Controls.right():
                    obj.pos_x += player_speed

                room_after_move = get_room_from_pos((obj.pos_x, obj.pos_y))
                if room_after_move != room_before_move:
                    game.move_camera_to_new_room(room_after_move)
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
        for obj in game.objects:
            resources.blt_sprite(obj.sprite, obj.pos_x, obj.pos_y)



init()
pyxel.run(update, draw)
