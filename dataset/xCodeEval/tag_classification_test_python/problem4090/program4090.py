    from sys import stdin, stdout
    ti = lambda : stdin.readline().strip()
    ma = lambda fxn, ti : map(fxn, ti.split())
    ol = lambda arr : stdout.write(' '.join(str(i) for i in arr) + '\n')
    os = lambda i : stdout.write(str(i) + '\n')
    olws = lambda arr : stdout.write(''.join(str(i) for i in arr) + '\n')
    
    
    n = int(ti())
    l = 1
    r = n
    ans = n
def ksuits(k, l, r, n):
    	cur = n
    	petya = 0
    	vasya = 0
    	while cur > 0:
    		o = min(cur, k)
    		vasya += o
    		cur -= o
    		cur -= cur/10
    	return vasya*2 >= n
    
    while l <= r:
    	k = (l+r)/2
    	if ksuits(k, l, r, n):
    		ans = k
    		r = k-1
    	else:
    		l = k+1
    os(ans)