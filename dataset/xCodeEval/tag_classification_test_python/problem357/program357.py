    import math
    
def nis():
        return map(int, input().split())
    
    k, r = nis()
    
    for i in range(1, 11):
        rem = (i * k) % 10
        if not rem or rem == r:
            break
    
    print(i)