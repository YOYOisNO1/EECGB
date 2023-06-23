    import sys
    import math
    import functools
    
    @functools.lru_cache(maxsize=None)
def sol(s):
    	ans = 0
    	for i in range(len(s)):
    		a = i > 0 and ord(s[i]) - ord(s[i-1]) == 1
    		b = i < len(s) -1 and ord(s[i]) - ord(s[i+1]) == 1
    		if a or b:
    			ans = max(ans, 1 + sol(s[:i] + s[i+1:]))
    	return ans
    
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()
    ans = sol(s)
    print(ans)