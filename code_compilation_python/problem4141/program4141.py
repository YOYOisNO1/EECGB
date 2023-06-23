    from sys import stdin, stdout
    
    n, m = map(int, stdin.readline().split())
    
    g = set()
    for i in range(m):
        a, b = map(int , stdin.readline().split())
        a -= 1
        b -= 1
        g.add((min(a, b), max(a, b)))
    
def check(k):
        for i in g:
            a = (i[0] + k) % n
            b = (i[1] + k) % n
            if not (min(a, b), max(a, b)) in g:
                return False
        return True
    
    for k in range(1, n):
        if n % k == 0:
            if not check(k):
                continue
            stdout.write('Yes')
            exit(0)
    
    stdout.write('No')