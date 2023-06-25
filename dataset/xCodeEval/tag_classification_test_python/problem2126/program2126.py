def w(N, K):
        a = [0]*(N+1)
        a[0] = 1
        for i in range (1, min(N, K)+1):
            a[i] = sum (a[0:i])
        if N > K:
            for x in range(K+1,N+1):
                a[x] = sum(a[x-K: x])
        return a[-1]
    
    
def sol():
        n, k, g = map(int, input().split(" "))
        result = (w(n, k)-w(n, g-1)) % (10**9+7)
        print(result)
    
    
    sol()
    
    