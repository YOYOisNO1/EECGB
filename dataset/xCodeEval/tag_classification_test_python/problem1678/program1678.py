def program1678():
    n,m=map(int,input().split())
    
    
    temp=0
    for x in range(1001):
        for y in range(1001):
            if (x*x+y)==n and (x+y*y)==m:
                temp+=1
    
    print(temp)            