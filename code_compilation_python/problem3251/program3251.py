def program3251():
    #http://codeforces.com/contest/888/problem/B
    n=int(input())
    s=input()
    l=r=u=d=0
    for i in s:
    	if i=='L':
    		l++
    	elif i=='R':
    		r++
    	elif i=='D':
    		d++
    	else:
    		u++
    
    ans=min(l,r)*2+min(u,d)*2
    print(ans)