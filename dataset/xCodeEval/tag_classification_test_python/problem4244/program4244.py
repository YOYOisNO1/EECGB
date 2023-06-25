    
def gcd(a,b):
        while(b>0):
            r=a%b
            a=b
            b=r
        return a 
    
    
    
    inp=lambda:map(int,input().split())
    x,y=inp()
    
    a,b=inp()
    
    
    
    r=a-(2*(x>a)-1)
    q=b-(2*(y>b)-1)
    
    print(2*max(abs(x-r),2)+2*max(abs(y-q),2))