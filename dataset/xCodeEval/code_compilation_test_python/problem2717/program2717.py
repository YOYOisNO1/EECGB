    u, v, a, b = map(int, input().split())
    A, B = {}, {}
    
def f(t):
        if t[1] == 0: return 0 if t[0] > a else 1
        if not t in A: A[t] = sum(g((t[1], t[0] - i)) for i in range(1, min(a, t[0]) + 1)) % 100000000
        return A[t]
    
def g(t):
        if t[1] == 0: return 0 if t[0] > b else 1
        if not t in B: B[t] = sum(f((t[1], t[0] - i)) for i in range(1, min(b, t[0]) + 1)) % 100000000
        return B[t]
    
    print((f((u, v)) + g((v, u))) % 100000000)