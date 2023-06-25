def program7451():
    n = int(input())
    a = [1,3,15,133,2025,37851,1030367,36362925,1606008513]
    if n % 2:
        ans = a[n/2]
        for i in xrange(n):
            ans *= (i + 1)
            ans %= 1000000007
        print(ans)
    else:
        print(0)