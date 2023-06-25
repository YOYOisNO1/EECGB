def program4595():
    n,k = map(int,input().split())
    t = input()
    k1 = set(t)
    d = {}
    for i in k1:
    	d[i] = (t.index(i),n-t[::-1].index(i)-1)
    s = set()
    for i in range(len(t)):
    	if i <= d[t[i]][1]:
    		s.add(t[i])
    	if len(s) > k:
    		print("YES")
    		exit()
    	if i == d[t[i]][1]:
    		s.remove(t[i])
    print("NO")