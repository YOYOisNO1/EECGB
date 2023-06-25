def program268():
    str0 = [int(i) for i in input().split()]
    n = str0[0]
    t = str0[1]
    k = str0[2]
    d = str0[3]
    baked = n
    t1 = 0
    while True:
        if baked < k:
            baked = 0
            t1 += t
        else:
            t1 += t
            baked -= k
        if baked == 0:
            break
    t2 = 0
    baked = n - n%k - k
    bakers = 1
    while True:
        if k > n:
            t2 = 1000000000000000000
            break
        t2 += 1
        if t2 == d:
            bakers = 2
        if t2%t == 0:
            baked -= k
            if baked == 0:
                break
        if bakers == 2:
            if (t2 - d)%t == 0:
                baked -= k
                if baked == 0:
                    break
    t2 += t
    if t2<t1:
        print("YES")
    else:
        print("NO")