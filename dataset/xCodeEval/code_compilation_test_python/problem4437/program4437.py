    Q, n, w, b = [10**9+9] + map(lambda x: int(x), input().split())
def pow(x, y) :
        if y == 1 : return x
        t = pow(x, y // 2)
        return t * t * (y % 2 == 1 and x or 1) % Q
    F = lambda x : reduce(lambda i, j : i * j % Q, xrange(2, x + 1), 1)
    G = lambda x: pow(F(x), Q - 2)
    print reduce(lambda x,i:x+(i-1)*F(w-1)*G(i-1)*G(w-i)*F(b-1)*G(n-i-1)*G(b+i-n),xrange(max(2,n-b),min(n,w+1)),0)*F(w)*F(b) % Q