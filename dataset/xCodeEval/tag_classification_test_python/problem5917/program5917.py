def gcd(a, b):
    	if a>b:
    		a, b=(b, a)
    	while a!=0:
    		a, b=(b%a, a)
    	return b
    n=int(input())
    crushes=[int(i)-1 for i in input().split()]
    cycles={i:-1 for i in range(n)}
    visited=set()
    c=-1
    failed=False
    cycle_lengths=set()
    for start in range(n):
    	if start not in visited:
    		visited.add(start)
    		c+=1
    		cycles[start]=c
    		next=crushes[start]
    		length=1
    		while next not in visited:
    			visited.add(next)
    			cycles[next]=c
    			next=crushes[next]
    			length+=1
    		cycle_lengths.add(length)
    		if next!=start:
    			failed=True
    			break
    if failed:
    	print(-1)
    else:
    	total=1
    	for i in cycle_lengths:
    		if i%2==0:
    			i=i//2
    		k=gcd(i, total)
    		total*=(i//k)
    	print(total)