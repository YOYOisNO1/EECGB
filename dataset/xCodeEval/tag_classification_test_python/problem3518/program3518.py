    from sys import stdin
    import copy
    lines = stdin.readlines()
    a,b,n = map(int,lines[0].split())
    flag = True
def gcd(x,y):
        c = min(x,y)
        for i in range(c,0,-1):
            if x % i == 0 and y % i == 0:
                return i
    
    flag2 = 0
    while flag:
        if flag2 == 0:
            n -= gcd(a,n)
        else:
            n -= gcd(b,n)
        if n == 0 and flag2 == 0:
            flag = False
            print(0)
        elif n == 0 and flag2 == 1:
            flag = False
            print(1)
        elif n < 0 and flag2 == 0:
            flag = False
            print(0)
        elif n < 0 and flag2 == 1:
            flag = False
            print(1)
        else:
            flag2 = abs(flag2-1)