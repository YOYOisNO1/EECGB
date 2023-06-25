    I=lambda:map(int, input().split())
    
def isok(a,b,k):
        if a<=k<=b: return 0
        elif k<a: return -1
        else: return 1
    
def bs(a,b,c,d,x,y):
        ans=[0,0]
        while a<=b:
            mid=(a+b)/2
            ret=isok(c,d,mid*y/x)
            if ret==0: ans=[mid,mid*y/x];a+=1
            elif ret==-1: a+=1
            else: b-=1
        return ans
    a,b,x,y=I()
    a0,b0,a1,b1=0,0,0,0
    a0,b0=bs(1,a,1,b,x,y)
    a1,b1=bs(1,b,1,a,y,x)
    if a0*b0<a1*b1: a0,b0=a1,b1
    print a0,b0