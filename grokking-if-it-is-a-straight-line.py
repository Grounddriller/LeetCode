def check_straight_line(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    dx = x2 - x1
    dy = y2 - y1

    for x3, y3 in coordinates[2:]:
        if dy * (x3 - x1) != dx * (y3 - y1):
            return False

    return True
