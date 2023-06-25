    a, b = map(int, input().split())
    
def rek(a, b):
    	if b > a:
    		a, b = b, a
    	res = min(a // 4, b) + (1 if ((a // 2) % 2) and b - a // 4 > 1 else 0)
    	if a >= 2 and b == 1:
    		return 1
    	if res == 0:
    		return 0
    	b -= res
    	a -= res * 2
    	return res + rek(a, b)
    print(rek(a, b))