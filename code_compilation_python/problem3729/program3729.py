    BASE = 998244353
    import heapq
    
    N = 2 * 10**5
    
    fac = [1]
    inv_fac = [1]
    
    for i in range(1, N + 1):
        fac.append((fac[-1] * i) % BASE)
        inv_fac.append((inv_fac[-1] * pow(i, BASE-2, BASE)) % BASE)
        assert (fac[i] * inv_fac[i] - 1) % BASE == 0
    
    
def fft(A,w):
        N=len(A)
        # assert (N & -N) == N
        if N<=1: return A
        even=fft(A[0::2],(w*w)%BASE)
        odd=fft(A[1::2],(w*w)%BASE)
        F=[0]*N
        x=1
        for j in range(0,N//2):
            F[j]=(even[j]+x*odd[j])%BASE
            F[j+N//2]=(even[j]-x*odd[j])%BASE
            x=(x*w)%BASE
        return F
    
def ifft(A,w):
        q = pow(len(A), BASE-2, BASE)
        return [(i*q)%BASE for i in fft(A, pow(w, BASE-2, BASE))]
    
    root_order, root = 524288, 363395222
    
def convolve(A,B):
        # assert len(A) & -len(A) == len(A)
        w = pow(root, root_order // len(A), BASE)
        # assert pow(w, len(A), BASE) == 1
        u=fft(A,w)
        v=fft(B,w)
        return [u%BASE for u in ifft([(u[i]*v[i])%BASE for i in range(len(u))],w)]
    
def stirling_row(n):
        k = min(n, K)
        # https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Explicit_formula
        # stirling(n, k) == inv_fac[k] * sum((-1)**(k - j) * binom(k, j) * (j**n) for j in range(k + 1))
        # = sum(((-1)**(k - j) * inv_fac[k - j]) * (inv_fac[j] * (j**n)) for j in range(k + 1))
    
        pad = (2 << (k.bit_length())) - (k + 1)
        A = [(pow(-1, j) * inv_fac[j]) % BASE for j in range(k + 1)] + [0] * pad
        B = [(pow(j, n, BASE) * inv_fac[j]) % BASE for j in range(k + 1)] + [0] * pad
        assert len(A) == len(B) == (len(A) & -len(A))
        R = convolve(A, B)
        return sum(R[1:k+1])
    
def solve(N, K):
        muls = [0] * (N + 1)
        Q = [1]
        QV = {1: 1}
    
        while len(Q):
            n_div = Q[0]; heapq.heappop(Q)
            mul = QV[n_div]
    
            n = (N - 1) // n_div + 1
            muls[n] += mul
    
            for i in range(2, n + 1):
                n2 = (N - 1) // (n_div * i) + 1
                if n2 <= 0: break
    
                child = n_div * i
                if child not in QV:
                    QV[child] = 0
                    heapq.heappush(Q, child) 
    
                QV[child] = QV.get(child, 0) - mul
    
    
        ans = 0
        for n in range(1, N + 1):
            c = muls[n]
            if c == 0: continue
            ans += c * stirling_row(n)
    
        return ans % BASE
    
    while True:
        try:
            line = input().strip()
            if len(line) == 0: continue
            N, K = list(map(int, line.split(" ")))
        except EOFError:
            break
    
        print(solve(N, K))
    