def program757():
    from math import sqrt
    a1,a2,a3 = list(map(int,input().split()))    #1e4
    a,b,c    = sqrt((a2*a3)/a1), sqrt((a1*a3)/a2), sqrt((a1*a2)/a3)
    print(4*int(a+b+c))