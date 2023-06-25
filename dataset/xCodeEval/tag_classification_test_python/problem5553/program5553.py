    
def within(a,b, c):
        return c>=a and c<=b
    
def isoverlap(diff, R1, r1, r2):
        if within(-r1,r1,diff-r2) and within (-r1,r1,diff+r2):
            return False
        if diff-r2<=-R1 and diff+r2>=R1:
            return False
        if diff+r2<=-R1:
            return False
        if diff-r2>=R1:
            return False
        return True
    
    x1,y1,r1,R1=map(int,input().split())
    x2,y2,r2,R2=map(int, input().split())
    
    diff=(abs(x1-x2)**2 + abs(y1-y2)**2)**.5
    c=0
    
    f=[True]*4
    
    if isoverlap(diff,R1,r1,r2):
        f[2]=False
    if isoverlap(diff,R1,r1,R2):
        f[3]=False
    if isoverlap(diff,R2,r2,r1):
        f[0]=False
    if isoverlap(diff,R2,r2,R1):
        f[1]=False
        
    print(len([x) for x in f if x==True])