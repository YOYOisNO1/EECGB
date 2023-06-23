def program118():
    import sys
    I = lambda :map(int,input().split())
    n = int(sys.stdin.read())
    a = list(I())
    MIN = float('inf')
    MAX = -MIN
    for i in range(1,n):
            MAX = max(MAX,a[i]-a[i-1])
    for i in range(1,n-1):
            y = max(MAX,a[i+1]-a[i-1])
            MIN = min(MIN,y)
    print(MIN)
    