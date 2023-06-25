    from sys import stdin
    from collections import deque
    #from math import sqrt, floor, ceil, log, log2, log10, pi, gcd, sin, cos, asin
def ii(): return int(stdin.readline())
def fi(): return float(stdin.readline())
def mi(): return map(int, stdin.readline().split())
def fmi(): return map(float, stdin.readline().split())
def li(): return list(mi())
def lsi():
        x=list(stdin.readline())
        x.pop()
        return x
def si(): return stdin.readline()
    ############# CODE STARTS HERE #############
    a=[]
    n, l, r=mi()
    while n>1:
        a.append(n%2)
        n//=2
    if n:
        a.append(1)
    a.reverse()
    #print(a)
    i, s, j=2, 0, 0
    while j<len(a):
        if a[j]:
            x=(l//i)*i+(i//2)
            if x<l:
                x+=i
            y=(r//i)*i+(i//2)
            if y<=r:
                y+=i
            s+=((y-x)//i)
        i+=i
        j+=1
    print(s)