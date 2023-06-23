    import math
     
def lcm(a, b):
        return int(a * b / math.gcd(a, b))
        
    t = int(input())
    for _ in range(t):
    	n = int(input())
    	ans = n-1
        for g in range(1,int(math.sqrt(n))+1):
            if (N % g == 0):
                ans = min(ans, N-g)
                if (g > 1): ans = min(ans, N-N/g)
    	print(n-ans,ans)