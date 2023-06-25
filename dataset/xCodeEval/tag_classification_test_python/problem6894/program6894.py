    """
    
    """
    
    x0, y0 = map(int, input().split())
    n = input()
    
    
def cdist(x, y):
        return x * x + y * y
    
    
    d0 = [0] * n                      #distance from bag
    d1 = [[0] * n for i in xrange(n)] #distance to everything
    d2 = []                           #coordinate for each item
    
    
    
    for i in xrange(n):
        x, y = map(int, input().split())
        d0[i] = cdist(x - x0, y - y0)
    
        for j in xrange(i):
            d1[i][j] = cdist(x - d2[j][0], y - d2[j][1])
            d1[j][i] = d1[i][j]
    
        d2.append((x,y))
    
    
    ref = [1 << i for i in xrange(n)]
    a = [None] * (1 << n)
    a[0] = 0
    dp = [0] * (1 << n)
    
    
    for i in xrange(1 << n):
        if a[i] is not None:
            for j in xrange(n):
                if i & ref[j] == 0:  #finding the exclusive pair in combination
    
                    """
                    2 Calculations
                    Given ori, A, B
    
                    Distance from ori -> A -> B -> A -> ori
    
                    Distance from ori -> A -> B -> ori
    
                    Take whichever lower
    
                    Given
                    ori - 1, 1
                    A - 4, 3
                    B - 3, 4
                    C - 0, 0
    
                    1st iter
                    the first segment - ori -> A -> ori
                    - tried grabbing second item
                    second segment - grab B - ori -> A -> B -> ori
                    
    
                    """
    
                    t = i + ref[j] #index of combination of having that item
                    if not a[t] or a[t] > a[i] + d0[j] * 2:
                        a[t] = a[i] + d0[j] * 2
                        dp[t] = i
    
                    for k in xrange(j + 1, n): #adding 2nd item to see if that was faster
                        if t & ref[k] == 0:
                            t2 = t + ref[k]
                            c = a[i] + d0[j] + d1[j][k] + d0[k]
                            if not a[t2] or a[t2] > c:
                                a[t2] = c
                                dp[t2] = i
    
                    break #break inner loop j
    
    
    
    z = (1 << n) - 1   #final optmized value will always be stored in last
    print(a[z])
    
    r = [0]
    while z > 0: #start from back
        t = z - dp[z]
        
        while t:
            x = -t & t  #isolate the right most bit
            """
            http://www.catonmat.net/blog/low-level-bit-hacks-you-absolutely-must-know/
            https://wiki.python.org/moin/BitManipulation
    
            negative bit / 2 complement - invert all bit and plus 1
            43
            101011
            8 bit -
            00101011
            inverse
            11010100 + 1
            = 11010101
            """
            t -= x
            i = 0
    
            while x > 0:
                i += 1
                x >>= 1
            r.append(i)
    
        z = dp[z]
        r.append(0)
    
    print(' '). join(map(str,r))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                    
                    