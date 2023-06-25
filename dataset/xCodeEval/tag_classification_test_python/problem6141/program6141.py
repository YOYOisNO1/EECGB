def program6141():
    x1, y1, x2, y2 = map(int, input().split())
    rook, bishop, king = 0, 0, 0
    if x1 == x2 or y1 == y2:
        rook = 1
    else:
        rook = 2
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    if (dx + dy) % 2:
        bishop = 0
    else:
        if dx != dy:
            bishop = 2
        else:
            bishop = 1
    king = max(dx, dy)
    print(rook,) bishop, king