def power(x, y, p) :
        res = 1     # Initialize result
     
        # Update x if it is more
        # than or equal to p
        x = x % p
         
        if (x == 0) :
            return 0
     
        while (y > 0) :
             
            # If y is odd, multiply
            # x with result
            if ((y & 1) == 1) :
                res = (res * x) % p
     
            # y must be even now
            y = y >> 1      # y = y/2
            x = (x * x) % p
             
        return res
        
    x = 1
    ans = 6
    mod = 1000000007
    n = int(input())
    for i in range(1, n):
        x *= 2
        ans = (ans * power(4,x, mod))%mod
    print(ans)