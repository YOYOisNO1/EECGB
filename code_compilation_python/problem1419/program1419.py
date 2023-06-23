def program1419():
    from sys import stdin, stdout
    d, s = map(int, stdin.readline().split())
    a, b = zip(*[[int(t) for t in l.split()] for l in stdin.readlines()])
    sa = sum(a)
    sb = sum(b)
    if sa <= s <= sb:
    	stdout.write('YES\n')
    	e = s - sa
    	for i in range(d):
    		add = min(b[i] - a[i], e)
    			e -= add
    			stdout.write(f"{a[i] + add} ")
    	else:
    		stdout.write('NO')