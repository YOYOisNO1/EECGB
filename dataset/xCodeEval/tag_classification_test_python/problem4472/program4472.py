def program4472():
    n,a = map(int,input().split())
    s =sorted (input())
    f = [s[0]]
    ans=0
    l = 0
    for i in range(a-1):
    	for j in range(n):
    		if ord(s[j]) > ord(f[l]) +1:
    			f.append(s[j])
    			l+=1
    			break
    if len(f) == a:
    	for x in f:
    		ans += (ord(x) -96)
    	print((ans))
    else:
    	print(-1)