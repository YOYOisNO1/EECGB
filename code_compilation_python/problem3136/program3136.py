def program3136():
        import math
        x=int(input())
        i=1
        while i*i <= x:
         if x%i<1==math.gcd(x//i,i):r=i
         i+=1
        print(r,x//r)