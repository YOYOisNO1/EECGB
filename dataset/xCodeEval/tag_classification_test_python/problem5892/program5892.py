def gcd(x, y):
    	if (x < y): return gcd(y, x)
    	if (y == 0): return x
    	return gcd(y, x%y)
    
def lcm(x, y):
    	return (x/gcd(x, y))*y;
    
def main():
    	n = int(input())
    	adj = map(int, input().split())
    	for u in range(n): adj[u] -= 1
    	deg = [0 for u in range(n)]
    	for x in adj: deg[x] += 1
    	for x in deg:
    		if (x != 1):
    			print(-1)
    			return
    	marked = [True for u in range(n)]
    	val = 1
    	for u in range(n):
    		if (marked[u] == False):
    			continue
    		v, sz = u, 0
    		while marked[v] == True:
    			marked[v] = False
    			sz += 1
    			v = adj[v]
    		if (sz%2 == 1):
    			val = lcm(val, sz)
    		else:
    			val = lcm(val, sz/2)
    	print(val)
    	return
    
    
    if (__name__ == "__main__"):
    	main()