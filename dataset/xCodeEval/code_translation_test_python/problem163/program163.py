def solve(a, s):
        a.sort()
        return sum(a[:-1]) <= s
    
    n, s = map(int, input().split())
    a = map(int, input().split())
    print('YES') if solve(a, s) else 'NO'
    