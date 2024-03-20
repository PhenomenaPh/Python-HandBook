def can_eat(pos1: tuple, pos2: tuple) -> bool:
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])

    return (dx, dy) in [(1, 2), (2, 1)]
