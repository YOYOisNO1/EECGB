def log2(n):
        i=0
        a=1
        while(a<=n):
            i+=1
            a*=2
        return i-1
    
    import math
    
def length(n):
        if n==0 or n==1:
            return 1
        else:
            m=int(log2(n)+1)
            return 2**m-1
    
def solve(n,l,m):
        u=length(n)                    # length of array of 0,1
        o=math.ceil(u/2)               # position of middle element
        if n==1:
            return 1 
        if n==0:
            return 0
    
        d,t=divmod(n,2)                # d = n//2 and t = n mod 2
        if(m<=o):                      # m before middle element
            if(m==o):                  # if middle element is the right-most
                if(l==o):
                    return t
                return solve(d,l,o-1)+t     # no of one's is one's from [l to (middle-1)] + value of middle element(0 or 1)
                                                                # as no of one's in middle is equal to middle element itself
            return solve(d,l,m)
        elif(l>=o):                    # l after middle element 
            if(l==o):                   
                return solve(d,1,m-o)+t
            return solve(d,l-o,m-o)
        else:                                          # l before middle and m after middle
            return solve(d,l,o-1)+solve(d,1,m-o)+t     # l < o < m 
    t=1
    # t=int(input())
    while(t>0):
        n,l,m = [int(x) for x in input().split()]
        print(solve(n,l,m))
        t-=1