def program2861():
    import math
    p1 = [-1, 0, 1, 0]
    p2 = [0, 1, 0, -1]
    
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    s1 = abs(x1-x2)**2 + abs(y1-y2)**2
    s2 = abs(x1-x3)**2 + abs(y1-y3)**2
    s3 = abs(x3-x2)**2 + abs(y3-y2)**2
    if ((s1+s2) == s3) or (s1+s3 == s2) or (s3+s2 == s1):
        print('RIGHT')
        exit()
    for i in range(3):
        for j in range(4):
            if i == 0:
                x = x1 + p1[j]
                y = y1 + p2[j]
                s1 = abs(x - x2) ** 2 + abs(y - y2) ** 2
                s2 = abs(x - x3) ** 2 + abs(y - y3) ** 2
                s3 = abs(x3 - x2) ** 2 + abs(y3 - y2) ** 2
                if ((s1 + s2 == s3) or (s1 + s3 == s2) or (s3 + s2 == s1)) and (s1 != 0) and (s2 != 0) and (s3 != 0):
                    print('ALMOST')
                    exit()
            if i == 1:
                x = x2 + p1[j]
                y = y2 + p2[j]
                s1 = abs(x1 - x) ** 2 + abs(y1 - y) ** 2
                s2 = abs(x1 - x3) ** 2 + abs(y1 - y3) ** 2
                s3 = abs(x3 - x) ** 2 + abs(y3 - y) ** 2
                if ((s1 + s2 == s3) or (s1 + s3 == s2) or (s3 + s2 == s1)) and (s1 != 0) and (s2 != 0) and (s3 != 0):
                    print('ALMOST')
                    exit()
            if i == 2:
                x = x3 + p1[j]
                y = y3 + p2[j]
                s1 = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
                s2 = abs(x1 - x) ** 2 + abs(y1 - y) ** 2
                s3 = abs(x - x2) ** 2 + abs(y - y2) ** 2
                if ((s1 + s2 == s3) or (s1 + s3 == s2) or (s3 + s2 == s1)) and (s1 != 0) and (s2 != 0) and (s3 != 0):
                    print('ALMOST')
                    exit()
    print('NEITHER')