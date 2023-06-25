    n = int(input())
def prime(n):
        i = 2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True
def smallestDivisor(n): 
        if (n % 2 == 0): 
            return 2; 
        i = 3;  
        while(i * i <= n): 
            if n%i==0:
                return i
            i += 2; 
        return n; 
    if (n&1)==0:
        print(n//2)
    else:
        if(prime(n)):
            print(1)
        else:
            ans = smallestDivisor(n)
            print(1+(n-ans)//2)