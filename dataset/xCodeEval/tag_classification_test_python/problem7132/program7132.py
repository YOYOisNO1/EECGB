    M = 10**9 + 7
    
    
def period(p, k):
        c = 1
        ek = k
        while ek != 1:
            ek = (ek * k) % p
            c += 1
        return c
    
    
def functions(p, k):
        if k == 0:
            return pow(p, p-1, M)
        elif k == 1:
            return pow(p, p, M)
        else:
            c = (p-1)//period(p, k)
            return pow(p, c, M)
    
    
    if __name__ == '__main__':
        p, k = map(int, input().split())
        print(functions(p, k))