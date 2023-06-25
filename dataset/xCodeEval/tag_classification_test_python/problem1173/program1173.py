def program1173():
    from random import random
    import math
    import re
    import fractions
    
    t = {"<":0,"^":1,">":2,"v":3}
    s, d = input().split(" ")
    n = input() % 4
    # print(n,) (t[d] - t[s]) % 4
    if n % 2 == 0:
        print("undefined")
    elif (t[d] - t[s]) % 4 == n:
        print("cw")
    elif (t[d] - t[s]) % 4 == (4 - n)%4:
        print("ccw")
    else:
        print("undefined")