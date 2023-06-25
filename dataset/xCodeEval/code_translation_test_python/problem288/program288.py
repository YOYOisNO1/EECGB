    from math import *
    from collections import deque
    from copy import deepcopy
    import sys
def inp(): return sys.stdin.readline().rstrip("\r\n") #for fast input
def multi(): return map(int,input().split())
def strmulti(): return map(str, inp().split())
def lis(): return list(map(int, inp().split()))
def lcm(a,b): return (a*b)//gcd(a,b)
def ncr(n,r): return factorial(n) // (factorial(r) * factorial(max(n - r, 1)))
def stringlis(): return list(map(str, inp().split()))
def out(var): sys.stdout.write(str(var))  #for fast output, always take string
def printlist(a) :
        print(' '.join(str(a[i]) for i in range(len(a))))
    
def isPrime(n) :
        if (n <= 1) : return False
        if (n <= 3) : return True
        if (n % 2 == 0 or n % 3 == 0) : return False
        i = 5
        while(i * i <= n) :
            if (n % i == 0 or n % (i + 2) == 0) :
                return False
            i = i + 6
        return True
    
    
    
    
    #copied functions end
    
    #start coding
    
    
def check(a,b,initiala,initialb,ans):
        if(len(a)!=len(initiala) or len(b)!=len(initialb)):
            return False
        for pair in zip(a,initiala):
            if pair[0]!=pair[1]:
                return False
    
        for pair in zip(b, initialb):
    
            if pair[0] != pair[1]:
                return False
    
        return True
    n=int(input())
    a=lis()
    b=lis()
    k1=a[0]
    k2=b[0]
    initiala=deepcopy(a[1:])
    initialb=deepcopy(b[1:])
    a=deque(a[1:])
    b=deque(b[1:])
    ans=0
    while(True):
        if(ans>200):
            print(-1)
            exit(0)
        if(len(a)==0 or len(b)==0):
            if(len(a)==0):
                print(ans,2)
            elif(len(b)==0):
                print(ans,1)
    
            exit(0)
    
        if(a[0]>b[0]):
            num1=a.popleft()
            num2=b.popleft()
    
            a.append(num2)
            a.append(num1)
            ans+=1
        else:
            num1 = a.popleft()
            num2 = b.popleft()
    
            b.append(num1)
            b.append(num2)
            ans += 1
    
    
        if(check(a,b,initiala,initialb,ans)):
            print(-1)
            exit(0)
    
    
    
    
    
    
    
    
    
    
    
    
    