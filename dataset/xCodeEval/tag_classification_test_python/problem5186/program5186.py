    n, l, r  = map(int, input().split())
        
def long(n):
        return 2**(len(bin(n))-2)-1
    
        
def sol(n, l, r):
        if r < l:
            return 0
        if n == 1 or n == 0:
            return n
        mitad = (long(n)-1)/2 
        if r < mitad+1:
            return sol(n/2,l,r)
        elif r == mitad+1:
            return sol(n/2,l,r-1) + n%2
        elif l > mitad+1:
            return sol(n/2, l-mitad-1, r-mitad-1)
        elif l == mitad+1:
            return sol(n/2, l-mitad-1, r-mitad-1) + n % 2
        else:
            return n%2 + sol(n/2,l,mitad) + sol(n/2,1,r-mitad-1)
    
    print(sol(n,l,r))