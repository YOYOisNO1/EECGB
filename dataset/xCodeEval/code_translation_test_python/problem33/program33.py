    #sys.setrecursionlimit(300000)
    import sys
    import math as m
def main():
        pass
def binary(n):
        #decimal to binary
        return (bin(n).replace("0b", ""))
def decimal(s):
        #binary to decimal
        return (int(s, 2))
def pow2(n):
        #power of a number base 2
        p = 0
        while n > 1:
            n //= 2
            p += 1
        return (p)
def isPrime(n):
        # if  number is prime in √n time
        if (n == 1):
            return (False)
        else:
            root = int(n ** 0.5)
            root += 1
            for i in range(2, root):
                if (n % i == 0):
                    return (False)
            return (True)
def lts(l):
        #list to string ,no spaces
        s=''.join(map(str,l))
        return s
def stl(s):
        #for each character in string to list with no spaces -->
        l=list(s)
        #for space in string  -->
        #l=list(s.split(" "))
        return l
    #Returns list of numbers with a particular sum
def sq(a,target,arr=[]):
        s=sum(arr)
        if(s==target):
            return arr
        if(s>=target):
            return
        for i in range(len(a)):
            n=a[i]
            remaining=a[i+1:]
            ans=sq(remaining,target,arr+[n])
            if(ans):
                return ans
    
    #1000000007
    mod=int(1e9)+7
def sinp(): return sys.stdin.readline().strip()
def iinp(): return int(input())
def ninp(): return map(int, sys.stdin.readline().strip().split())
def llinp(): return list(map(int, sys.stdin.readline().strip().split()))
def p(xyz): print(xyz)
def p2(a,b):print(a,b)
    #for _ in range(iinp()):
    a,b,c,d=ninp()
    m1=max(3*a/10,a-(a/250)*c)
    m2=max(3*b/10,b-(b/250)*d)
    if(m1==m2):
        print("Tie")
    elif(m1>m2):
        print("Misha")
    else:
        print("Vasya")