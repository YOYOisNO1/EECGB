    inf = 1000 * 1000 * 1000
def calc(x, y):
    	if(x % a != 0 or y % b != 0):
    		return inf
    	if(x == 0 && y == 0):
    		return 0
    	s = x / a + y / b
    	if(s % 2 == 1):
    		return inf
    	if(x < a || y < b):
    		return inf
    	return max(x / a, y / b)
    n, m, x, y, a, b = map(int, input().split())
    ans = calc(x-1, y-1)
    ans = min(ans, calc(x-1, m-y))
    ans = min(ans, calc(n-x, y-1))
    ans = min(ans, calc(n-x, m-y))
    ans = int(ans)
    print(ans if ans != inf else 'Poor Inna and pony!')