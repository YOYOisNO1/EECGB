def primefactors(x):
        ans = []
        i = 2
        while i*i <= x:
            if x%i==0:
                ans.append(i);
                while x%i==0:
                    x = x//i
            i = i+1
        if x>1:
            ans.append(x)
        return ans
    
    x , n = [int(c) for c in input().split()]
    prime = primefactors(x)
    MOD = 1000000007
    ans = 1
    for x in prime:
        p = 0
        tmp = x
        while tmp <= n:
            p = p + n//tmp
            tmp = tmp*x
        ans = ans*pow(x , p , MOD)
    ans = ans%MOD
    print(ans)