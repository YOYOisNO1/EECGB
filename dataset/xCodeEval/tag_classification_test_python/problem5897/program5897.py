def lcm(a, b):
    	return a * b // gcd(a, b)
    
def gcd(a, b):
    	if a < b:
    		a, b = b, a
    	if b == 0:
    		return a
    	else:
    		return gcd(a % b, b)
    
    n = int(input())
    arr = list(map(lambda x: int(x) - 1, input().split()))
    v = [0] * n
    m = []
    flag = 0
    for i in range(n):
    	if v[i] == 0:
    		t = 1
    		j = i
    		while arr[j] != i:
    			j = arr[j]
    			t += 1
    			if v[j] == 1:
    				flag = 1
    				break
    			v[j] = 1
    		if flag:
    			break
    		v[i] = 1
    		t = t // 2 if t % 2 == 0 else t
    		m.append(t)
    if flag:
    	print(-1)
    else:
    	s = 1
    	for a in m:
    		s = lcm(s, a)
    	print(s)