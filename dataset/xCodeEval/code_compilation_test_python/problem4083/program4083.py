    import sys
    
    sys.setrecursionlimit(10 ** 6)
    int1 = lambda x: int(x) - 1
    p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
    
    class mint:
    def __init__(self, x):
            self.__x = x % md
    
    def __repr__(self):
            return str(self.__x)
    
    def __neg__(self):
            return mint(-self.__x)
    
    def __add__(self, other):
            if isinstance(other, mint): other = other.__x
            return mint(self.__x + other)
    
    def __sub__(self, other):
            if isinstance(other, mint): other = other.__x
            return mint(self.__x - other)
    
    def __rsub__(self, other):
            return mint(other - self.__x)
    
    def __mul__(self, other):
            if isinstance(other, mint): other = other.__x
            return mint(self.__x * other)
    
        __radd__ = __add__
        __rmul__ = __mul__
    
    def __truediv__(self, other):
            if isinstance(other, mint): other = other.__x
            return mint(self.__x * pow(other, md - 2, md))
    
    def __rtruediv__(self, other):
            return mint(other * pow(self.__x, md - 2, md))
    
    def __pow__(self, power, modulo=None):
            return mint(pow(self.__x, power, md))
    
    md = 998244353
    
def nCr(com_n, com_r):
        if com_n < com_r: return 0
        return fac[com_n] * ifac[com_r] * ifac[com_n - com_r]
    
    n_max = 200005
    fac = [mint(1)]
    for i in range(1, n_max + 1): fac.append(fac[-1] * i)
    ifac = [mint(1)] * (n_max + 1)
    ifac[n_max] /= fac[n_max]
    for i in range(n_max - 1, 1, -1): ifac[i] = ifac[i + 1] * (i + 1)
    
def main():
        n,k=MI()
    
        if k>n-1:
            print(0)
            exit()
    
        ans=0
        for i in range(n-k):
            ans+=nCr(n-k,n-k-i)*pow(n-k-i,n,md)*(-1)**(i&1)
        ans*=nCr(n,n-k)
        if k>0:ans*=2
    
        print(ans)
    
    main()