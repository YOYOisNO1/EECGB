def program6126():
    r1, c1, r2, c2 = [int(i) for i in input().split()]
    dr = abs(r1 - r2)
    dc = abs(c1 - c2)
    result = [0] * 3
    
    result[0] = 1 if dr == 0 or dc == 0 else 2
    if dr == dc:
        result[1] = 1
    elif (dr + dc) % 2 == 1:
        result[1] = 0
    else:
        result[1] = 2
    result[2] = max(dr, dc)
    print(" ".join([str(i) for i in result]))