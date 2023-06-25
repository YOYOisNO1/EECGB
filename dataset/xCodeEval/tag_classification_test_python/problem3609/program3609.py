def program3609():
    from sys import stdin, stdout
    ti = lambda : stdin.readline().strip()
    ma = lambda fxn, ti : map(fxn, ti.split())
    ol = lambda arr : stdout.write(' '.join(str(i) for i in arr) + '\n')
    os = lambda i : stdout.write(str(i) + '\n')
    olws = lambda arr : stdout.write(''.join(str(i) for i in arr) + '\n')
    
    
    n, t = ma(int, ti())
    s = list(ti())
    
    for j in range(t):
    	i = 0
    	while i < n-1:
    		if s[i] == 'B' and s[i+1] == 'G':
    			s[i], s[i+1] = s[i+1], s[i]
    			i += 1
    		i += 1
    olws(s)