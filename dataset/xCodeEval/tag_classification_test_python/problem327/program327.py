def program327():
    from random import random
    import math
    import re
    import fractions
    
    # N = input()
    M, D = map(int, input().split(" "))
    
    dom = [31,28,31,30,31,30,31,31,30,31,30,31]
    print(int(math.ceil((float(dom[M-1]-(8-D)))/7)+1))