def program337():
    import math as mt;
    a,b=map(int,input().split());
    
    print(int(min(a,mt.floor((-1+mt.sqrt(1+8*(240-b)/5))/2))))