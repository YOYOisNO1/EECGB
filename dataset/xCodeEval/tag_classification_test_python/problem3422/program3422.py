def ni():
        return int(input())
    
def nis():
        return map(int, input().split())
    
def si():
        return input()
    
    n, m = nis()
    
    if m > n:
        print(-1)
    elif not n % (2 * m):
        print(n) / 2
    else:
        print(m) * (n / (2 * m) + 1)
    