    # from math import gcd
    from math import *
     
    # Function to find the nCr
     
     
def NcK(n, r):
     
        # p holds the value of n*(n-1)*(n-2)...,
        # k holds the value of r*(r-1)...
        p = 1
        k = 1
     
        # C(n, r) == C(n, n-r),
        # choosing the smaller value
        if (n - r < r):
            r = n - r
     
        if (r != 0):
            while (r):
                p *= n
                k *= r
     
                # gcd of p, k
                m = gcd(p, k)
     
                # dividing by gcd, to simplify product
                # division by their gcd saves from
                # the overflow
                p //= m
                k //= m
     
                n -= 1
                r -= 1
     
            # k should be simplified to 1
            # as C(n, r) is a natural number
            # (denominator should be 1 )
     
        else:
            p = 1
     
        # if our approach is correct p = ans and k =1
        return(p)
     
    # for _ in range(int(input())):
    #     # n = int(input())
    #     # L = input().rstrip('\n')
    #     n,a,b = list(map(int,input().split()))
     
    a,b = list(map(float,input().split()))
    # k = (a-1)*b
    # if int(k) == k:
    #     print(int(k))
    # else:
    #     print(int(k)+1)                            
     
     
    a = int(a)
    n = a
    A = NcK(int(a),3)
    if b == 0:
        print(0)
    elif (NcK(n-1,2)/A)*0.5>=b:
        print((1))
    elif (n-2)/A + (NcK(n-1,2)/A)*0.5 >= b:
        print(2)
     
     
    else:
        # a1 = NcK(a-1,3)
        # a2 = NcK(a-1,2)  
        # A = NcK(int(a),3)
        # a11 = NcK(a-2,3)
        # if (a1/A)*1+(a2/A)*1>=b and :
        #     print(a-1)  
        flag = False                    
        for i in range(3,int(a)-1):
            a1 = NcK(i,3)
            a2 = NcK(i,2) 
            a3 = NcK(i,1)
            a33 = NcK(a-i,2)
            A = NcK(int(a),3)
            if (a1/A)*1+(a2*(a-i)/A)*1+(a3*a33/A)*0.5>b:
                print(i)
                flag = True
                break
        if not flag:
            print(a-1)