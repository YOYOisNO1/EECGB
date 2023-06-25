    import math
    from fractions import gcd
def inp():
        return int(input())
def linp():
        return map(int, input().split())
    n, x, y = linp()
    if n==2:
        print("NO")
    else:
        n/=2
        li = [[n, n], [n, n+1], [n+1, n], [n+1, n+1]]
        for i in li:
            if x==i[0] and y==i[1]:
                print("NO")
                exit()
        print("YES")