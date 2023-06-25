    # q1
    
    from collections import defaultdict
    from math import sqrt,factorial,gcd,log2,inf,ceil
    # map(int,input().split())
    # l = list(map(int,input().split()))
    mod = 10**9 + 7
    
    
    q 3
def solve(n):
        odd = 0
        even = 0
        for i in range(2,int(sqrt(n))+1):
            if n%i == 0:
                z = n//i
                if i%2 == 0:
                    even+=1
                else:
                    odd+=1
    
                if z!=i and z%2 == 0:
                    even+=1
                elif z!=i and z%2!=0:
                    odd+=1
    
        return even,odd
    
    
    
    
    n = int(input())
    e,o = solve(n)
    if e == 0 and o == 0:
        print(n)
    else:
        if o == 0 or e == 0:
            print(2)
        else:
            print(1)
    
    
    
    