def fall_fac(n,k):
    	ans = 1
    	for i in range(k):
    		ans *= n-i
    	return ans
def C(n,k):
    	if not(0 <= k <= n):
    		return 0
    	else:
    		return fall_fac(n,k)//fall_fac(k,k)
def derangement(n):
    	if n==0:
    		return 1
    	elif n==1:
    		return 0
    	else:
    		return (n-1)*(derangement(n-1)+derangement(n-2))
    n, k = [int(x) for x in input().split()]
    print(sum([C(n,i)*derangement(i) for i in range(k+1)]))