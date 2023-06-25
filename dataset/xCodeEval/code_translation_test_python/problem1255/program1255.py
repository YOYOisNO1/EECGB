    n, k = map(int, input().split())
    p = [1, 1]
    for i in range(2,n+1): p.append(p[i - 1] + p[i - 2])
    
def tim(k, n, x):
    	#print("---%d %d %d") %(k, n, x)
    	if n == 0: return 0
    	if k == 0: return 0
    	if k <= p[n-1]:
    		print(x) + 1,
    		tim(k, n - 1, x + 1)		
    	else:
    		print(x) + 2, x + 1,
    		tim(k - p[n - 1], n - 2, x + 2)		
    tim(k, n, 0)