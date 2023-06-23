    a, b, c = map(int, input().split(' '))
    mod = 998244353
    
def calc (a, b) :
    	if a > b:
    		a, b = b, a
    	ans = 0
    	tmp = 1
    	for i in range(a + 1):
    		ans = (ans + tmp) % mod
    		tmp = tmp * (a - i) * (b - i) * pow(i + 1, mod - 2, mod) % mod
    	return ans
    
    ans = calc(a, b) * calc(b, c) * calc(a, c) % p
    
    print(ans)