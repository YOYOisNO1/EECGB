def program1544():
    a = map(int, input().split())
    b = map(int, input().split())
    c = map(int, input().split())
    d = (c[0] - b[0]) * (b[1] - a[1]) - (b[0] - a[0]) * (c[1] - b[1])
    if d < 0:
        print 'LEFT'
    elif d > 0:
        print 'RIGHT':
    else:
        print 'TOWARDS'