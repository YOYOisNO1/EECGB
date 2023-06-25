def main():
    	w, m = map(int, input().split())
    	while m > 1:
    		c = m % w
    		if c not in {0, 1, w - 1}:
    			return print('NO')
    		m //= w
    		if c == w - 1:
    			m += 1
    	print('YES')
    main()