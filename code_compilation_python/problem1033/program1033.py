def program1033():
    ﻿n=int(input())
    import math
    a=(-1+math.sqrt(1+8*n))/2
    a=floor(a)
    c=(a*(a+1))//2
    print(a+(n-c))