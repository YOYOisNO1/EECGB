def program2242():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    
    x1 = 0
    for i in a:
        x1 += i
        if(x1 >= 180): break
    
    x2 = 360 - x1
    diff = x1 - x2
    
    for i in a:
        x1 -= i
        x2 += i
        diff = min(diff,abs(x1-x2))
    
    print(diff)