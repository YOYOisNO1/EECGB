def comb(n,m):
        if m > n:
            return 0
        else:
            x = 1
            for i in range(n,n-m,-1):
                x *= i
    
            for i in range(1,m+1):
                x /= i
            return x
    
    n= input()
    
    print(comb(n,5)) * comb(n,5) * 120