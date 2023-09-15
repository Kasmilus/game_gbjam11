import math
from typing import List, Tuple
from enum import Enum

from game_object import Obj, ObjType
from room import *


class GameState(Enum):
    Splash = 1,
    PressToStart = 2,
    Game = 3


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

    player_obj: Obj = None  # Reference to the player



game: Game = Game()
