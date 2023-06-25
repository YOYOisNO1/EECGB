    import math 
     
def findPowerPrime(fact, p): 
        res = 0
        while fact:  
            res += fact // p 
            fact //= p 
     
        return res 
     
     
def findPowerComposite(fact, n): 
        
        res = math.inf 
     
        for i in range(2, int(n**0.5) + 1): 
     
            count = 0
            if not n % i: 
                count += 1
                n = n // i 
     
            if count: 
     
                curr_pow = findPowerPrime(fact, i) // count 
                res = min(res, curr_pow) 
        if n >= 2: 
            curr_pow = findPowerPrime(fact, n) 
            res = min(res, curr_pow) 
     
        return res 
     
     
     
def primeFactors(n): 
         
        ans = set()
        while n % 2 == 0: 
            ans.add(2)
            n = n // 2
              
        for i in range(3,int(math.sqrt(n))+1,2): 
              
            # while i divides n , print(i) ad divide n 
            while n % i== 0: 
                # print(i,) 
                ans.add(i)
                n = n // i 
        if n > 2: 
            # print(n) 
            ans.add(n)
     
        return ans
     
     
    x, n = map(int, input().split())
     
    pf = primeFactors(x)
     
    ans = 1
     
     
     
    
    for i in pf:
        # print(i)
        tmp = findPowerComposite(n, i)
        ans *= pow(i, tmp, 1000000007)
        ans = ans%1000000007
     
    print(ans)