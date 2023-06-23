def program481():
    from sys import stdin
    n,a,b =map(int,stdin.readline().split())
    c = map(int,stdin.readline().split())
    ans = 0
    if n%2 and c[n/2]==2:
        ans = min(a,b)
    for i in xrange(n/2):
        if c[i]!=c[n-i-1]:
            if c[i]==2:
                ans += min(a,b)
            else c[n-1-i]==2:
                ans += min(a,b)
            else:
                ans=-1
                break
        elif c[i]==2:
            ans += 2*min(a,b)
    print ans