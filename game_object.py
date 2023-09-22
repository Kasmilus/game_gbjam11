from typing import List, Tuple, TypedDict, Optional
from enum import Enum

import pyxel

from constants import *
import utils

class ObjType(Enum):
    Undefined = 0
    Player = 1
    World = 3
    PlayerHook = 4
    Decor = 5
    Coin = 6
    Key = 7
    Door = 8
    Checkpoint = 9

    ParticleRun = 10
    ParticleExplosion = 11

    EnemyFlying = 12
    EnemyWalking = 13

    Water = 14

    Text = 15


class Obj:
    def __init__(self, obj_type: ObjType, sprite: Tuple[int, int], pos: Tuple[int, int], name:str = "Unknown", collides: bool = True, is_hookable: bool = False, bounding_box: Tuple[int, int, int, int] = None, text: str = None):
        self.name = name
        self.obj_type = obj_type
        self.sprite = sprite
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.last_move_dir = (1, 0)  # Always start facing right
        self.velocity = (0, 0)  # When launched by a hook
        self.velocity_drag = 0.5
        self.hook_velocity = None  # hook only
        self.is_hookable = is_hookable
        self.is_hooked = False
        self.is_pushable = False
        self.collides = collides
        self.last_input_frame = 0  # for anim
        self.collided_during_hook = False
        self.death_timer = None
        self.text = text
        self.started_roll_hooked = False

        if bounding_box is None:
            self.bounding_box = (0, 0, GRID_CELL_SIZE, GRID_CELL_SIZE)
        else:
            self.bounding_box = bounding_box
        self.draw_priority = 0  # The higher, the later it will be drawn (on top of others)
        self.anim_speed = 18
        self.last_facing_dir_anim = 1

        # Player specific
        if obj_type == ObjType.Player:
            self.bounding_box = (5, 7, GRID_CELL_SIZE-5, GRID_CELL_SIZE)
            self.draw_priority = 3
            self.player_speed = 0
            self.player_dash_timer = 0
            self.player_hook_speed = 90  # Pixels per sec
            self.player_max_hooks = 5
            self.player_available_hooks = self.player_max_hooks
            self.is_pushable = True
            self.anim_speed = 90  # 1.5sec per frame
            self.player_collected_coins = 0
            self.player_collected_keys = 0
            self.player_last_checkpoint_name = "---"
            self.player_particle_count = 0

        # Hook
        if obj_type == ObjType.PlayerHook:
            self.bounding_box = (6, 6, GRID_CELL_SIZE-6, GRID_CELL_SIZE-6)  # Smaller than sprite!
            self.draw_priority = 5
            self.hook_drag = 1.4  # slowdown per sec
            self.hook_move_back_speed = None  # Set on create
            self.hook_attached_object = None  # Set on contact

        # Enemies
        if obj_type == ObjType.EnemyFlying:
            self.draw_priority = 4
            self.bounding_box = (5, 4, GRID_CELL_SIZE-5, GRID_CELL_SIZE)
            self.enemy_speed = 0.40
        if obj_type == ObjType.EnemyWalking:
            self.draw_priority = 4
            self.bounding_box = (2, 3, GRID_CELL_SIZE-2, GRID_CELL_SIZE-1)
            self.enemy_speed = 0.30

        if obj_type == ObjType.Decor:
            self.collides = False
            self.draw_priority = 0

        if obj_type == ObjType.World:
            self.draw_priority = 1

        if obj_type == ObjType.Coin:
            self.anim_speed = 12
            self.collides = False

        if obj_type == ObjType.Key:
            self.anim_speed = 50
            self.collides = False

        if obj_type == ObjType.Checkpoint:
            self.checkpoint_used = False

        if obj_type == ObjType.ParticleRun:
            self.last_input_frame = pyxel.frame_count
            self.anim_speed = 5
            self.particle_lifetime = (len(self.sprite)-1) * self.anim_speed
            self.collides = False
            self.particle_invert = False
            self.particle_invert_y = False
            self.draw_priority = 4
        if obj_type == ObjType.ParticleExplosion:
            self.last_input_frame = pyxel.frame_count
            self.anim_speed = 4
            self.particle_lifetime = (len(self.sprite)-1) * self.anim_speed
            self.collides = False
            self.particle_invert = pyxel.rndi(0, 1) == 1
            self.particle_invert_y = pyxel.rndi(0, 1) == 1
            self.draw_priority = 2  # Above world, below characters

        if obj_type == ObjType.Text:
            self.draw_priority = 2  # Above world, below characters
            self.collides = False
            self.name = "Tutorial Text"

    def __repr__(self):
        pos = int(self.pos_x / GRID_CELL_SIZE), int(self.pos_y / GRID_CELL_SIZE)
        return f"[OBJ] {self.name} ({pos[0]}, {pos[1]})"

    def get_pos(self) -> Tuple[int, int]:
        return self.pos_x, self.pos_y
    def get_pos_mid(self) -> Tuple[int, int]:
        return self.pos_x + HALF_GRID_CELL, self.pos_y + HALF_GRID_CELL
    def get_bbox_world_space(self) -> Tuple[int, int, int, int]:
        return self.pos_x + self.bounding_box[0], self.pos_y + self.bounding_box[1], self.pos_x + self.bounding_box[2], self.pos_y + self.bounding_box[3]

    def get_hook_attach_point(self, game) -> Tuple[int, int]:
        x_dir = game.player_obj.pos_x - self.pos_x
        y_dir = game.player_obj.pos_y - self.pos_y
        tmp_bbox = self.bounding_box[0] - 1, self.bounding_box[1] - 1, self. bounding_box[2] + 1, self.bounding_box[3]
        if x_dir < 0:
            x = tmp_bbox[0]
        elif x_dir > 0:
            x = tmp_bbox[2]
        else:
            x = tmp_bbox[0] + (tmp_bbox[2] - tmp_bbox[0])/2
        if y_dir < 0:
            y = tmp_bbox[1]
        elif y_dir > 0:
            y = tmp_bbox[3]
        else:
            y = tmp_bbox[1] + (tmp_bbox[3] - tmp_bbox[1])/2
        return self.pos_x + x, self.pos_y + y

    def get_render_sprite(self) -> Tuple[int, int]:
        render_sprite = self.sprite
        if type(render_sprite) is list:
            render_sprite = render_sprite[int((pyxel.frame_count - self.last_input_frame) / self.anim_speed) % len(render_sprite)]
        return render_sprite


def collision_bb(pos_a: Tuple[int, int], bb_a: Tuple[int, int, int, int], pos_b: Tuple[int, int], bb_b: Tuple[int, int, int, int]) -> bool:
    collides = pos_a[0] + bb_a[0] < pos_b[0] + bb_b[2] and \
               pos_a[0] + bb_a[2] > pos_b[0] + bb_b[0] and \
               pos_a[1] + bb_a[1] < pos_b[1] + bb_b[3] and \
               pos_a[1] + bb_a[3] > pos_b[1] + bb_b[1]
    return collides

def objs_can_collide(obj_a: Obj, obj_b: Obj) -> bool:
    if obj_a is obj_b:
        return False
    if obj_a.collides is False:
        return False
    if obj_b.collides is False:
        return False

    # Allow rolling into the water (or out of it)
    if obj_a.started_roll_hooked or obj_b.started_roll_hooked:
        if obj_a.obj_type is ObjType.Player and PLAYER_DASH_TIME-0.13 < obj_a.player_dash_timer < PLAYER_DASH_TIME:
            if obj_b.obj_type is ObjType.Water:
                return False
        if obj_b.obj_type is ObjType.Player and PLAYER_DASH_TIME-0.13 < obj_b.player_dash_timer < PLAYER_DASH_TIME:
            if obj_a.obj_type is ObjType.Water:
                return False

    return True

def collision_obj(obj_a: Obj, obj_b: Obj) -> bool:
    if not objs_can_collide(obj_a, obj_b):
        return False
    return collision_bb(obj_a.get_pos(), obj_a.bounding_box, obj_b.get_pos(), obj_b.bounding_box)


def _line_intersection_distance(x1, y1, x2, y2, x3, y3, x4, y4) -> Tuple[float, float]:
    denominator = ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))

    if denominator == 0:
        return -1, -1

    u_a = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator
    u_b = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator
    return u_a, u_b

def get_line_intersection_point(line_a_start: Tuple[float, float],line_a_end: Tuple[float, float], line_b_start: Tuple[float, float],line_b_end: Tuple[float, float],) -> Optional[Tuple[float, float]]:
    u_a, u_b = _line_intersection_distance(line_a_start[0], line_a_start[1], line_a_end[0], line_a_end[1],
                                           line_b_start[0], line_b_start[1], line_b_end[0], line_b_end[1])
    if 0 <= u_a <= 1 and 0 <= u_b <= 1:
        intersection_x = line_a_start[0] + (u_a * (line_a_end[0]-line_a_start[0]))
        intersection_y = line_a_start[1] + (u_a * (line_a_end[1]-line_a_start[1]))
        return intersection_x, intersection_y

    return None

def get_line_bb_intersection_point(line_start: Tuple[float, float],line_end: Tuple[float, float], bb: Tuple[int, int, int, int],) -> Optional[Tuple[float, float]]:
    a = get_line_intersection_point(line_start, line_end, (bb[0], bb[1]), (bb[2], bb[1]))
    if a is not None:
        return a
    b = get_line_intersection_point(line_start, line_end, (bb[0], bb[1]), (bb[0], bb[3]))
    if b is not None:
        return b
    c = get_line_intersection_point(line_start, line_end, (bb[0], bb[3]), (bb[2], bb[3]))
    if c is not None:
        return c
    d = get_line_intersection_point(line_start, line_end, (bb[2], bb[1]), (bb[2], bb[3]))
    if d is not None:
        return d

    return None

def get_dist_obj(obj_a: Obj, obj_b: Obj) -> float:
    # TODO: Use bbox center?
    return utils.get_vector_len((obj_b.pos_x - obj_a.pos_x, obj_b.pos_y - obj_a.pos_y))

def check_obj_move_collision(obj_a: Obj, obj_b: Obj, move_dir: Tuple[int, int]) -> Tuple[int, int]:
    """ Note: you probably want to pass in normalised move_dir!"""
    if not objs_can_collide(obj_a, obj_b):
        return move_dir
    move_dir = [move_dir[0], move_dir[1]]
    if collision_bb((obj_a.pos_x + move_dir[0], obj_a.pos_y), obj_a.bounding_box, obj_b.get_pos(), obj_b.bounding_box):
        move_dir[0] = 0
    if collision_bb((obj_a.pos_x, obj_a.pos_y + move_dir[1]), obj_a.bounding_box, obj_b.get_pos(), obj_b.bounding_box):
        move_dir[1] = 0

    return move_dir[0], move_dir[1]

