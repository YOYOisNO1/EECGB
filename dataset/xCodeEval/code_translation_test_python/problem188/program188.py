def program188():
    import math
    n = int(input())
    r = [int(n) for n in input().split()]
    b = [int(n) for n in input().split()]
    d = sum(r) - sum(b) - 1
    big = [r[i] for i in range(n) if r[i] > b[i]]
    if d > 0:
        print('1')
    elif len(big) == 0:
        print('-1')
    else:
        score = sum(big) - d
        print(math.ceil(score / len(big)))