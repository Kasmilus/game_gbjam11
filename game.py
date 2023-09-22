import math
from typing import List, Tuple
from enum import Enum

from game_object import Obj, ObjType
from room import *


class GameState(Enum):
    Splash = 1,
    PressToStart = 2,
    Game = 3,
    GameOver = 4


class Game:
    def __init__(self):
        self.game_state: GameState = GameState.Game
        #self.game_state: GameState = GameState.Splash
        self.all_objects: List[Obj] = []  # List of all objects in game
        self.objects: List[Obj] = []  # List of only objects in current and surrounding rooms
        self.objects_decor: List[Obj] = []

        self.splash_timer: float = 0
        self.press_to_start_timer: float = 0
        self.played_splash_sound: int = 0

        self.camera_x: int = 0
        self.camera_y: int = 0
        self.camera_target_x: int = 0
        self.camera_target_y: int = 0
        self.camera_move_timer: float = 0

        self.player_obj: Obj = None  # Reference to the player

        self.stop_frames: int = 0

        self.time_since_game_over: int = 0
        self.return_to_game: bool = False


def init_game():
    global game
    global game_checkpoint
    game = Game()
    game_checkpoint = None

