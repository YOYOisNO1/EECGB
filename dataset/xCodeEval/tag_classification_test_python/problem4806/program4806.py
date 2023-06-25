def program4806():
    import math
    n=int(input())
    e=int(math.sqrt(n))
    if(n%e==0):
        extra=0
    else:
        extra=1
    print(int((e*2)+(2*(n//e+(extra)))))