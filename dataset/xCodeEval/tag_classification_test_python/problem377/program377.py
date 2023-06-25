def program377():
    # import sys 
    # sys.stdin=open("input.in",'r')
    # sys.stdout=open("out.out",'w')
    n,a=map(int,input().split())
    t=list(map(int,input().split()))
    x=t[a-1]
    i=a-2
    p=2*a-2-i
    while i>=0 and p<n:
    	if t[i] and t[p]:
    		x+=t[i]+t[p]
    	i-=1
    	p=2*a-2-i
    if p==n:
    	x+=sum(t[0:i+1])
    else:
    	x+=sum(t[p:])
    print(x)