    import sys
    
def koning(x1,y1,x2,y2):
        return max(abs(x2-x1),abs(y2-y1))
    
def toren(x1,y1,x2,y2):
        if x1==x2 or y1==y2:
            return 1
        else:
            return 2
    
def loper(x1,y1,x2,y2):
        if abs(x1-y1)%2!=abs(x2-y2)%2:
            return 0
        else:
            if abs(r1-r2)==abs(c1-c2):
                return 1
            else:
                return 2
    
    r1,c1,r2,c2=map(int,input().split())
    
    
    print(toren(r1,c1,r2,c2),loper(r1,c1,r2,c2),koning(r1,c1,r2,c2))