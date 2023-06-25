    import math as mt 
    import sys,string,bisect
    input=sys.stdin.readline
    from collections import deque,defaultdict
    L=lambda : list(map(int,input().split()))
    Ls=lambda : list(input().split())
    M=lambda : map(int,input().split())
    I=lambda :int(input())
def dist(x,y,c,d):
        return mt.sqrt((x-c)**2+(y-d)**2)
def circle(x1, y1, x2,y2, r1, r2): 
      
        distSq = (((x1 - x2)* (x1 - x2))+ ((y1 - y2)* (y1 - y2)))**(.5) 
      
        if (distSq + r2 <= r1): 
            return True
        else: 
            return False
    n=I()
    l=L()
    d=1
    c=0
    x=0
    for i in range(1,n):
        if(i>=2):
            if(l[i-2]==3 and l[i-1]==1 and l[i]==2):
                x+=1
        if(l[i-1]==2 and l[i]==3 or (l[i-1]==3 and l[i]==2)):
            print("Infinite")
            d=0
            break
        elif(l[i-1]==1):
            if(l[i]==2):
                c+=3
            else:
                c+=4
        elif(l[i-1]==2):
            if(l[i]==1):
                c+=3
        elif(l[i-1]==3):
            if(l[i]==1):
                c+=4
    if(d):
        print("Finite")
        print(c-x)
               
        