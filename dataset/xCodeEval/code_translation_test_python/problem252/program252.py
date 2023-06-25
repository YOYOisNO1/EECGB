    import math
def prime(n):
        ok= True
        for i in range(2, int(math.sqrt(n))):
            if(n%i==0):
                ok = False
                break
        if(ok):
            return True
        else:
            return False
def fact(a,b):
        ans = 1
        for i in range(a, b+1):
            ans*= i
        return str(ans)-1
def comb(n, c):
        return fact(n)//(fact(n-c)*c)
    
    a,b = map(int, input().split())
def done(c,d):
        if(c==0 or d==0):
            return True
        else:
            return False
    while(not done(a,b)):
        if(a >= 2*b):
            a = int(a%(2*b))
        else:
            if(b >= 2*a):
                b = int(b%(2*a))
            else:
                break
    print(a,b)