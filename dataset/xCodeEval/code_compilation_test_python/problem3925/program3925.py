def f(L,n):
    	i = n-1
    	if i==0:
    		return L*c[0]
    	v1 = f(L,n-1)
    	v2 = (L+l[i]-1)//l[i]*c[i]
    	v3 = L//l[i]*c[i] + f(L%l[i],n-1)
    	return min(v1,v2,v3)
    
    n, L = map(int, input().split())
    c = list(map(int, input().split()))
    l = [2**i for i in range(n)]
    print(f(L,n))