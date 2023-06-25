def power(x, y, p):
        res = 1
        x = x % p
        if (x == 0) :
            return 0
        while (y > 0) :
            if ((y & 1) == 1) :
                res = (res * x) % p
            y = y >> 1  
            x = (x * x) % p
             
        return res
        
    t = int(input())
    for _ in range(t):
        n , k = map(int,input().split())
        ans = 1
        p = 1000000007
        if n%2==0:
            x_partial = power(2,n-1,p)
            
            x = (x_partial + p-1)%p
            y = (x_partial*2)%p
            
            ans = power(x,k,p)
            for i in range(0,k):
                ans = (ans + (power(x,i,p)*power(y,k-1-i,p))%p)%p
     
            print(ans)
        
        else:
            x = power(2,n-1,p) + 1
            ans = power(x,k,p)
            print(ans)
     