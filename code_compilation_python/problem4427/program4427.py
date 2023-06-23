    x=0;
    y=0;
    
def f(n):
    	if(n==1):return x
    	if(n%2==1):return min(f(n-1)+x,f(n+1)+x)
    	else:return min(f(n/2)+y,f(n/2)+x*n/2)
    
    n,x,y=map(int,input().split())
    print f(n)