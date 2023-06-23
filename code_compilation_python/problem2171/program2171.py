    
    from math import sqrt,gcd
def primeFactors(n):
    
        # Print the number of two's that divide n
        sa = []
        while n % 2 == 0:
            sa.append(2)
            n = n / 2
    
        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        for i in range(3,int(sqrt(n))+1,2):
    
            # while i divides n , print i ad divide n
            while n % i== 0:
                sa.append(int(i))
                n = n / i
    
                # Condition if n is a prime
        # number greater than 2
        if n > 2:
            sa.append(int(n))
        return list(set(sa))
    
    
    
    
    
    from math import sqrt
    from collections import defaultdict
    from bisect import bisect_right
def ncr(n, r, p):
        num = den = 1
        for i in range(r):
            num = (num * (n - i)) % p
            den = (den * (i + 1)) % p
        return (num * pow(den,
                          p - 2, p)) % p
    
    
    
def cal(n):
        seti = set()
        for i in range(2,int(sqrt(n))+1):
            if n%i == 0:
                seti.add(n//i)
                seti.add(i)
    
    
        return seti
    
    
def pre(s):
    
        n = len(s)
    
        lps = [0]*(n)
    
    
        for i in range(1,n):
            j = lps[i-1]
    
            while j>0 and s[i]!=s[j]:
                j = lps[j-1]
    
            if s[i] == s[j]:
                j+=1
            lps[i] = j
        for i in range(1,n):
            if lps[i] == i+1:
                lps[i]-=1
    
        return lps
    
    
    from collections import defaultdict
def solve():
    
        x,y,z = map(int,input().split())
    
        x1,y1,z1 = map(int,input().split())
        m = sqrt(x1**2 + y1**2 + z1**2)
        m1 = sqrt((x1-x)**2 + (y1-y)**2 + (z1-z)**2)
        a1,a2,a3,a4,a5,a6 = map(int,input().split())
    
        ans = 0
        if y<0:
            z5 = abs(y/m)
            if 0.5<=z5<=1:
                ans+=a1
    
        if y>y1:
            z5 = abs((y-y1)/m1)
            # print(z)
            if 0.5<=z5<=1:
                ans+=a2
    
        if z<0:
            z5 = abs(z/m)
            if 0.5<=z5<=1:
                ans+=a3
    
        if z>z1:
            z5 = abs((z-z1)/m1)
    
            if 0.5<=z5<=1:
                ans+=a4
    
        if x<0:
            z5 = abs(x/m)
            if 0.5<=z5<=1:
                ans+=a5
    
        if x>x1:
            z5 = abs((x-x1)/m)
            if 0.5<=z5<=1:
                ans+=a6
    
    
        print(ans)
    
    
    
    # t = int(stdin.readline())
    # for _ in range(t):
    solve()
    
    