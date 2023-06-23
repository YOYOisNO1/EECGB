def program3423():
    n = int(input())
    a = map(int, input().split())
    
    s = 0
    for i in xrange(n):
        if a[i] == 1:
            s += 1
        elif a[i] == 0 and (i > 0 and i + 1 < n and a[i-1] == 1 and a[i+1] == 1):
            s += 1
    
    print s