def program6450():
    from itertools import permutations
    n = int(input())
    a = int(input())
    b = int(input())
    
    res = 10 ** 10
    for sides in permutations([a] * 4 + [b] * 2):
        curRes = 0
        rest = 0
        for side in sides:
            if side > rest:
                rest = n
                curRes += 1
            rest -= side
        res = min(res, curRes)
    
    print(res)