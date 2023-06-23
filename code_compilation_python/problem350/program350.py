def program350():
    a,b = map(int,input().split())
    s = list(map(int,input().split()))
    s1 = list(map(int,input().split()))
    k = min(s)
    k1 = min(s1)
    t = []
    for i in range(max(a,b)):
    	if a>=b:
    		if s[i] in s1:
    			t.append(s1[i])
    	if b>a:
    		if s1[i] in s:
    			t.append(s[i])
    if len(t):
    	print(min(t))
    elif k != k1:
    	print(10*min(k,k1)+max(k,k1))