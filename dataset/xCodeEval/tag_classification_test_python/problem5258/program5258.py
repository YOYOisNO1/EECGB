    #!/usr/bin/env python
    from sys import stdin as cin
    
    M = 1000000007
    
def count_words(n, m):
    	r = 1
    	for i in range(n):
    		r = (r * m) % M
    	return r
    
    
def main():
    	n, m, k = map(int, next(cin).split())
    
    	if n < k:
    		return count_words(n, m)
    		return 0
    
    	if n == k:
    		return count_words((n + 1) // 2, m)
    		
    	if k == 1:
    		return count_words(n, m)
    
    	if k % 2 == 0:
    		return m
    	else:
    		return m*m
    
    
    print(main())