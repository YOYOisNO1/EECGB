    #!/usr/bin/env python
    """(c) gorlum0 [at] gmail.com"""
    from __future__ import division
    import itertools as it
    from sys import stdin
    
def solve(n, m):
        if n > m: n, m = m, n
        if n == 1: return m
        if n == 2:
            q, r = divmod(m, 4)
            return q*4 + min(r, 2)*2
        return (n*m + 1)//2
    
def main():
        for l in stdin:
            n, m = map(int, l.split())
            print(solve(n,) m)
    
    if __name__ == '__main__':
        main()