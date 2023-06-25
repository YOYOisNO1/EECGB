def program4854():
    a,b=map(int,input().split())
    c,x,d=0,1,a-b
    while x*x<=d:
    	if d%x==0:
    		c+=(x>b)+(x*x<d and d/x>b)
    	x+=1
    print'infinity'if d==0 else c
    