def program385():
    n = int( input() )
    ans = 0
    for i in xrange( 1, n+1 ):
        ans += 1 << i
    print(ans)