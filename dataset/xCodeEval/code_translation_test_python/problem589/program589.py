def nir(n):
        if n < 10:
            return max(1,n)
        else:
            p = nir(n//10)*(n%10)
            q = nir(n//10-1)*9
            return max(p,q)
    
    n = int(input())
    ans = nir(n)
    print(ans)