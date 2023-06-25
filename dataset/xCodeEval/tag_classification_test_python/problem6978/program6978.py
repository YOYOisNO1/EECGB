    
def f(N, M):
        num = M*(M-1)*(M-2)//6 + M*(M-1)*(N-M)//2 + M*(N-M)*(N-M-1)/4
        den = N*(N-1)*(N-2)//6
        return num/den 
    
def process(N, P):
        if P==0:
            return 0
        if P==1:
            return N-1
        s = 0
        e = N-1
        while s+1 < e:
            m = (s+e)//2
            if f(N, m) < P:
                s, e = m, e
            else:
                s, e = s, m
        return e
    
    N, P = input().split()
    N = int(N)
    P = float(P)
    print(process(N, P))