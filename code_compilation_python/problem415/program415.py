    import math
    
def modInverse(b,m): 
        g = math.gcd(b, m)  
        if (g != 1): 
            # print("Inverse doesn't exist")  
            return -1
        else:  
            # If b and m are relatively prime,  
            # then modulo inverse is b^(m-2) mode m  
            return pow(b, m - 2, m) 
      
      
    # Function to compute a/b under modulo m  
def modDivide(a,b,m): 
        a = a % m 
        inv = modInverse(b,m) 
        if(inv == -1): 
            print("Division not defined") 
        else: 
            return (inv*a) % m
    for z in range(1):
        n =int(input())
        ans=0
        r= n*(n+1)//6
        p=998244353
        print(modDivide(r,2**n,p))
        