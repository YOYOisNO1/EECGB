    import sys
    
    f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"
    
    s1 = "What are you doing while sending \""
    s2 = "\"? Are you busy? Will you send \""
    s3 = "\"?"
    
    a=[75]
    
    for i in range(53):
    	var = 68 + 2*a[i]
    	a.append(var)
    
def seek(n, k):
    	t = k
    	if n == 0:
    		if t < 75:
    			return f0[t]
    		else:
    			return '.'
    	if 0 <= t < 34:
    		return s1[t]
    	t = t - 34
    	if 0 <= t < a[n-1]:
    		return seek(n - 1, t)
    	t = t - a[n-1]
    	if 0 <= t < 32:
    		return s2[t]
    	t = t - 32
    	if 0 <= t < a[n-1]:
    		return seek(n - 1, t)
    	t = t - a[n-1]
    	if 0 <= t < 2:
    		return s3[t]
    	return '.'
    
    
    while True:
    	q = int(input())
    	for i in range(q):
    		n,k = map(int,input().split())
    		print(seek(n,k-1),end="")
    	print()
    except EOFError:
    	pass