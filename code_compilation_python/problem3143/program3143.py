def program3143():
    n = int(input())
    res = [n]
    for i in range(n-1,0,-1):
        if all(y % i == 0 for y in res):
            res.append(i)
    print(' '.join([str(i) for i in res])