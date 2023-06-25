    import sys
    range = xrange
    input = input
    
    # Not super happy with this code but it is kinda cool. Look at the last line in the bottom.
    
    MOD = 10**9+7
def polysub(P,Q):
        n = len(P)
        m = len(Q)
        W = [0]*max(m,n)
        for i in range(n):
            W[i] += P[i]
        for i in range(m):
            W[i] -= Q[i]
        W = [w%MOD for w in W]
        while W and W[-1]==0:W.pop()
        return W
    
    # Polydiv (floored)
def polydiv(P,Q):
        while Q[-1]%MOD==0:Q.pop()
        assert(Q[-1]%MOD>0)
        P = P[:]
        ans = []
        n = len(Q)
        while len(P)>=n:
            p = P[-1]*pow(Q[-1],MOD-2,MOD)
            ans.append(p)
            for i in range(n):
                P[-i-1] -= p*Q[-i-1]
            assert(P[-1]%MOD==0)
            P.pop()
        W = [w%MOD for w in ans[::-1]]
        while W and W[-1]==0:W.pop()
        return W
    
    # Polymod
def polymod(P,Q):
        while Q[-1]%MOD==0:Q.pop()
        assert(Q[-1]%MOD>0)
        P = P[:]
        n = len(Q)
        while len(P)>=n:
            p = P[-1]*pow(Q[-1],MOD-2,MOD)
            for i in range(n):
                P[-i-1] -= p*Q[-i-1]
            assert(P[-1]%MOD==0)
            P.pop()
        P = [p%MOD for p in P]
        #while P and P[-1]==0:P.pop()
        return P
    
def polyprod(P,Q):
        n = len(P)
        m = len(Q)
        W = [0]*(n+m-1)
        for i in range(n):
            for j in range(m):
                W[i+j]+=P[i]*Q[j]
        return [w%MOD for w in W]
    
    # return (g,x,y): P*x+b*y = g
def polyxgcd(P,Q):
        if len(P)<=1:
            return (Q,[],[1])
        g,x,y = polyxgcd(polymod(Q,P),P)
        return (g,polysub(y,polyprod(polydiv(Q,P),x)),x)
    
    # Calc A^m * B 
def power(A,B,m,mult):
        if m == 0:
            return B
        while m>1:
            if m%2==1:
                B = mult(A,B)
            A = mult(A,A)
            m//=2
        return mult(A,B)
        
def calc_nth_term(init,linear_coeff,n):
    def mult(A,B):
            return polymod(polyprod(A,B),linear_coeff)
        
        ans = power([0,1],[1],n,mult)
        return sum(ans[i]*init[i] for i in range(len(ans)))
    
    # Extrapolate an sequence finding the n-th term
    # This is only possible if the sequence follows a linear
    # recursion of at most half the length of the sequence
    
    # This will calculate the n-th term of the sequence 
def extrapolate(seq,n):
        twom = [0]*(len(seq)+1)
        twom[-1] = 1
        _,C,_ = polyxgcd(seq,twom)
        while C[-1]%MOD==0:C.pop()
        invc = pow(C[0],MOD-2,MOD)
        C = [c*invc%MOD for c in C]
        return calc_nth_term(seq,C[::-1],n)
    
    n,m = [int(x) for x in input().split()]
    
    mem = [-1]*201
def DP(n):
        if n<=0 or m==1:
            return 0 if n<0 else 1
        if mem[n]<0:
            mem[n] = DP(n-1) + DP(n-m)
        return mem[n]
    
    print(extrapolate([DP(i)) for i in range(201)],n)%MOD