def solve(n,ans):
    	
    	if n!=N:
    		solve(n+1,ans+l[n])
    		solve(n+1,ans-l[n])
    	else:
    		res.append(ans)
    
    N=int(input())
    res=[]
    l=[]
    for i in xrange(N):
    	l.append(int(input()))
    solve(0,0)
    ans=False
    for i in res:
    	if i%360==0:
    		ans=True
    		print('YES')
    		break
    if not ans:
    	print('NO')