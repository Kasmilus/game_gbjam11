from typing import List, Tuple

from game_object import ObjType
import game

"""
Does not work - probably because the game technically is not cell based 
so when Im checking if a "cell" is blocked, Im getting things wrong?
"""


def find_path(from_pos: Tuple[int, int], to_pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    if from_pos == to_pos:
        return []

    class Cell:
        def __init__(self, pos, parent=None, g=float('inf'), h=float('inf')):
            self.pos: Tuple[int, int] = pos
            self.parent = parent
            self.g: float = g
            self.h: float = h
            self.f: float = self.g + self.h

        def __eq__(self, other):
            return self.pos == other.pos

        def is_in_list(self, ls):
            for i in ls:
                if i.pos == self.pos:
                    return i
            return None

    def calculate_h(from_pos, to_pos) -> float:
        return abs(to_pos[0]-from_pos[0]) + abs(to_pos[1]-from_pos[1])

    def is_cell_blocked(pos):
        for obj in game.game.objects:
            if obj.collides and obj.get_cell() == pos:
                if obj.obj_type in [ObjType.EnemyFlying, ObjType.EnemyWalking]:
                    continue
                return True
        return False

    def return_path(cell):
        path: List[Tuple[int, int]] = [cell.pos]
        cell_parent = cell.parent
        while cell_parent is not None:
            path.append(cell_parent.pos)
            cell_parent = cell_parent.parent
        return path


    closed_list = []
    open_list = []

    start_cell = Cell(from_pos, g=0, h=0)
    open_list.append(start_cell)

    while len(open_list) > 0:
        p = open_list.pop(0)
        closed_list.append(p)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 and j != 0) or (i == 0 and j == 0):
                    continue  # Skip diagonals

                test_cell = Cell(pos=(p.pos[0]+i, p.pos[1]+j), parent=p)
                if test_cell.pos[0] == to_pos[0] and test_cell.pos[1] == to_pos[1]:
                    return return_path(test_cell)


                elif test_cell.is_in_list(closed_list) is None and is_cell_blocked(test_cell.pos) is False:
                    g_new = p.g + 1
                    h_new = calculate_h(test_cell.pos, to_pos)
                    test_cell.g = g_new
                    test_cell.h = h_new
                    test_cell.f = g_new + h_new
                    cell_in_list = test_cell.is_in_list(open_list)
                    if cell_in_list is not None:
                        if cell_in_list.f > test_cell.f:
                            open_list.remove(cell_in_list)
                            open_list.append(test_cell)
                    else:
                        open_list.append(test_cell)
    return []  # Not found

