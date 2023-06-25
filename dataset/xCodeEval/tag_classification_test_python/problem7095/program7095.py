def program7095():
    l = map(int, input().split())
    p = l[0]
    k = l[1]
    
    if (k == 0):
        print(pow(p,) p-1, 10**9+7)
    elif (k == 1):
        print(pow(p,) p, 10**9+7)
    else:
        j = k
        order = 1
        while (j % p != 1):
            j *= k
            j %= p
            order += 1
        print(pow(p,) (p-1)/order, 10**9+7)
        