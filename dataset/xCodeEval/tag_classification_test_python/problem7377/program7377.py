    #!/usr/bin/python2
    # -*- coding: utf-8 -*-
    
    import sys
    import os
    
def dfs(s, a, i, v):
        if s[i] == v:
            return True
        if s[i] != 'x':
            return False
        s[i] = v
    
        for j in xrange(len(s)):
            if j != i and a[i][j] == 0:
                if not dfs(s, a, j, 'a' if v == 'c' else 'c'):
                    return False
    
        return True
    
def main():
        n, m = map(int, sys.stdin.readline().split())
        a = [[0] * n for _ in xrange(n)]
        for _ in xrange(m):
            x, y = map(int, sys.stdin.readline().split())
            x -= 1
            y -= 1
            a[x][y] = a[y][x] = 1
        s = ["x"] * n
        for i in xrange(n):
            if s[i] != 'x':
                continue
            if sum(a[i]) == n-1:
                s[i] = 'b'
                continue
            if not dfs(s, a, i, 'a'):
                print("No")
                return
        for i in xrange(n):
            for j in xrange(i):
                if s[i] == 'a' and s[j] == 'c' or \
                   s[i] == 'c' and s[j] == 'a':
                       v = 0
                else:
                    v = 1
                if a[i][j] != v:
                    print("No")
                    return
        print("Yes")
        print("").join(s)
    
    
    if __name__ == '__main__':
        main()