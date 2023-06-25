def program968():
    
    
    from math import ceil,sqrt
    from collections import defaultdict
    from itertools import permutations
    n = int(input())
    
    a1,a2,a3 = map(int,input().split())
    b1,b2,b3 = map(int,input().split())
    
    ans1 = 10**18
    ans2 = min(a1,b2) + min(a2,b3) + min(a3,b1)
    per = [['a1','b1'],['a2','b2'],['a3','b3'],['a1','b3'],['a2','b1'],['a3','b2']]
    
    z = permutations(per)
    
    for i in z:
        x1,x2,x3 = a1,a2,a3
        y1,y2,y3 = b1,b2,b3
        # print(i)
        for a,b in i:
            if a == 'a1' and b == 'b1':
                z = min(x1,y1)
                x1-=z
                y1-=z
    
            if a == 'a2' and b == 'b2':
                z = min(x2,y2)
                x2-=z
                y2-=z
    
            if a == 'a3' and b == 'b3':
                z = min(x3,y3)
                x3-=z
                y3-=z
    
            if a == 'a1' and b == 'b3':
                z = min(x1,y3)
                x1-=z
                y3-=z
    
            if a == 'a2' and b == 'b1':
                z = min(x2,y1)
                x2-=z
                y1-=z
    
            if a == 'a3' and b == 'b2':
                z = min(x3,y2)
                x3-=z
                y2-=z
    
        ans1 = min(ans1,x1+x2+x3)
    print(ans1,ans2)
    
    