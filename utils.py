def clamp(val: float, a: float, b: float) -> float:
    if val < a:
        val = a
    if val > b:
        val = b
    return val


def clamp01(val: float) -> float:
    return clamp(val, 0, 1)

def sign(a):
    return (a>0) - (a<0)