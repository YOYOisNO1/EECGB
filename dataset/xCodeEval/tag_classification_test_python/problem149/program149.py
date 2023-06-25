def solve(n, m):
        sieve = [True]*(m+1)
        for i in range(2, len(sieve)):
            if sieve[i]:
                jump = i*i
                while jump < m+1:
                    sieve[jump] = False
                    jump += i
        n += 1
        while n <= m:
            if sieve[n] and n != m:
                return "NO"
            n += 1
                
        if sieve[m]:
            return "YES"
        else:
            return "NO"
            
    params = map(int, input().split())
    n = params[0]
    m = params[1]
    print(solve(n,) m)