    from sys import stdin
    import fractions
    
def line():
        return stdin.readline().split()
def read_int():
        return int(line()[0])
def read_ints():
        return [int(x) for x in line()]
def memo(fn):
        table = {}
    def memoized(*args):
            if args not in table:
                table[args] = fn(*args)
            return table[args]
        return fn
    
def solve(n, m, k):
        if (n - m)*k >= n:
            return n
    
        skips = (n - m)
        n -= skips*k
        doubles, last = n / k, n % k
        #print last, skips, doubles
    
        score = 0
        for _ in range(doubles):
            score += k
            score *= 2
            score = score % 1000000009
    
        score += (k - 1) * skips
        score = score % 1000000009
        score += last
    
        return score
    
    n, m, k = read_ints()
    print solve(n, m, k)