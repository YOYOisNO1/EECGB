    import math
    firstLine = input().split()
    A = int(firstLine[0])
    B = int(firstLine[1])
    N = int(firstLine[2])
    #a, b, n = map(int, input().split())
    
    MOD = 1000000007
    mySum = 0
    fact = [1, 1]
    lastFact = 1
    for x in xrange(2, N+1):
        fact.append(fact[x-1] * x % MOD)
    
def isGood(A, B, N):
        while N:
            if x%A != A and x%B != B:
                return False
            x /= 10
        return True
        
    for n in xrange(N+1):
        newNum = n*A + (N-n)*B
        if isGood(A, B, newNum):
            div = pow(fact[n]*fact[N-n], MOD-2, MOD)
            mySum += div
            mySum %= MOD
            #print mySum, fact[N], fact[N-n]
        
    print mySum*fact[N] %MOD