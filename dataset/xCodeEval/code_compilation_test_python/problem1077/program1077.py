def poss(n,a,b,x):
    	if n>=2 and n<=(a//x+b//x):
    		return True
    	else:
    		return False
    n,a,b=map(int, input().split())
    ans=1
    end=(a+b)//n
    while True:
    	if poss(n,a,b,ans) and not poss(n,a,b,ans+1):
    		print(ans)
    		exit(0)
    	else:
    		ans=(ans+end)//2