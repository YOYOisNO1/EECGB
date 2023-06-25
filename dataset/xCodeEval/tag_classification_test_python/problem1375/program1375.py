    import math
    
def nC2(n):
        if n <= 0:
            return 0
        if n%2 == 0:
            ans = int(n/2)
            ans *= (n-1)
        else:
            ans = int((n-1)/2)
            ans *= n
    
        return ans
    
def main():
        n,m = map(int,input().split())
    
        k = int(math.floor(n/m))
        #print((k))
        kmin = (n%m)*nC2(k+1)
        kmin += (m-(n%m))*nC2(k)
        #print(n+1-m)
        kmax = nC2(n+1-m)
    
        print((kmin,kmax))
    
    main()