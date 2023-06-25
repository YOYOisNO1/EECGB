def program4436():
    from math import factorial as F
    n, w, b = map(lambda x: int(x), input().split())
    print reduce(lambda x,i:x+(i-1)*F(w-1)/F(i-1)/F(w-i)*F(b-1)/F(n-i-1)/F(b+i-n),xrange(max(2,n-b),min(n,w+1)),0)*F(w)*F(b) % (10**9+9)