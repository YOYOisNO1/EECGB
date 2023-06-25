def program3495():
    k = input().split()
    n = int(k[0])
    m = int(k[1])
    k = int(k[2])
    
    if ( k <= n+m-2 ):
        if ( k < n ):
            outn = int((n / (k + 1)) * m)
        else:
            outn = int(m / (k - n + 2))
        if ( k < m):
            outm = int( m / ( k + 1)) * n
        else:
            outm = int( n / ( k - m + 2 )
        print (max( outn, outm))
    print -1