def program3170():
    a,b,c=list(map(int,input().split()))
    ans = 0
    while (a>!=0):
    	if c>b and b>a:
    		ans+=7
    	a-=1
    	b-=2
    	c-=4
    print(ans)