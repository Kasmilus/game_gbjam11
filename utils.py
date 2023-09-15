def clamp(val: float, a: float, b: float) -> float:
    if val < a:
        val = a
    if val > b:
        val = b
    return val


def clamp01(val: float) -> float:
    return clamp(val, 0, 1)


def collision(pos_x: int, pos_y: int, posb_x: int, posb_y: int, size: int = 16, sizeb: int = 16) -> bool:
    collides = pos_x < posb_x + sizeb and \
            pos_x + size > posb_x and \
            pos_y < posb_y + sizeb and \
            pos_y + size > posb_y
    return collides