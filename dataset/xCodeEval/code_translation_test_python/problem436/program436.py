    from fractions import *
def main():
        L = [ int(i) for i in input().split(" ")]
        a,b,n = L
        while True:
            n -= gcd(n,a)
            if n < 0:
                print(1)
                return
    
            n -= gcd(n,b)
                    
            if n < 0:
                print(0)
                return
    
    
    main()