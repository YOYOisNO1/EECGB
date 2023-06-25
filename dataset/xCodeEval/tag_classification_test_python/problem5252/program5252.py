    #!/usr/bin/python3
    
    MOD = int(1e9 + 7)
    N, m, k = [int(x) for x in input().split()]
def kelk(a, b):
    	ret = 1
    	while b:
    		if b % 2:
    			ret = (a*int(ret))%MOD
    
    		a = int(a*a)%MOD
    		a = int(a) % MOD
    		b //= 2
    
    	return int(ret) % MOD
    
    if k > N or k == 1:
    	print(kelk(m, N))
    elif k < N:
    	print(int(m + m*(m - 1)*(k % 2)))
    elif k == N:
    	print(kelk(m, (N+1)//2))