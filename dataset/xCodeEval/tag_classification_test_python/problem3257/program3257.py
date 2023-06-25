    import itertools as it
    import re
    from math import *
def rt():
        return input()
def rn():
        return int(input())
def rns():
        return map(int,input().split())
    
    
def isGood(n):
        s=bin(n)
        if len(s)%2==0:
            return False
        else:
            l=len(s[2:])/2
            if '1'*(l+1)+'0'*l==s[2:]:
                return True
            else:
                return False
    
    n=rn()
    '''
    a=[]
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            a.append(i)
            a.append(n/i)
    '''
    mx=1
    good=[1, 6, 28, 120, 496, 2016, 8128, 32640, 130816, 523776]
    for i in good:
        if n%i==0:
            mx=i
    print(mx)
        