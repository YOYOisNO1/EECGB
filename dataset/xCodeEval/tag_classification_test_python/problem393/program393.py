def program393():
    #In the name of Allah
    
    from sys import stdin, stdout
    input = stdin.readline
    
    r, x, y, _x, _y = map(int, input().split())
    
    r *= 2
    
    from math import ceil
    ans = ceil(((_x - x) ** 2 + (_y - y) ** 2) ** .5 / r)
    stdout.write(str(ans))