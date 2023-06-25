    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    
    # max
    a1, a3, a2 = a
    b1, b3, b2 = b
    wins = 0
    
    t = min(a1, b3)
    wins += t
    a1 -= t
    b3 -= t
    t = min(a2, b1)
    wins += t
    a2 -= t
    b1 -= t
    t = min(a3, b2)
    wins += t
    a3 -= t
    b2 -= t
    
    maxx = wins
    
    # min
def f(a1,a3,a2,b1,b3,b2,flag):
        if flag==1:
            t = min(a1, b3)
            # wins += t
            a1 -= t
            b3 -= t
        if flag==2:
            t = min(a1, b1)
            # draws += t
            a1 -= t
            b1 -= t
        if flag==3:
            t = min(a3, b3)
            # draws += t
            a3 -= t
            b3 -= t
        if flag==4:
            t = min(a3, b2)
            # wins += t
            a3 -= t
            b2 -= t
        if flag==5:
            t = min(a2, b1)
            # wins += t
            a2 -= t
            b1 -= t
        if flag==6:
            t = min(a2, b2)
            # draws += t
            a2 -= t
            b2 -= t
        return a1,a3,a2,b1,b3,b2
    
    
    import itertools
    perms = list(itertools.permutations([1, 2, 3, 4, 5, 6]))
    wins = float('inf')
    for perm in perms:
        b1, b3, b2 = a
        a1, a3, a2 = b
        for num in perm:
            a1,a3,a2,b1,b3,b2 = f(a1,a3,a2,b1,b3,b2,num)
        wins = min(wins, min(a1, b2)+min(a2, b3)+min(a3, b1))
    
    minn = wins
    print(minn, maxx)