def program628():
    n = int(input())
    s = input()
    best = 0
    a = set()
    for i in range(n):
    	if s[i].islower():
    		a.add(s[i])
    	if s[i].isupper() or i==n-1:
    		best = max(best , len(a))
    		a = set()
    print(best)