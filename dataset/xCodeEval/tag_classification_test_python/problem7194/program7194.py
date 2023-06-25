def program7194():
    ax, ay = map(int, input().split(' '))
    bx, by = map(int, input().split(' '))
    cx, cy = map(int, input().split(' '))
    cp = (ax-bx)*(cy-by)-(ay-by)*(cx-bx)
    if cp < 0:
        print("LEFT")
    if cp == 0:
        print("TOWARDS")
    if cp > 0:
        print("RIGHT")