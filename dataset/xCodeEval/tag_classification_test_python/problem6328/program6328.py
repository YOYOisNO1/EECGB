    from math import *
def sqr (f):
        return(sqrt(f)==int(sqrt(f)))
        
def bine(x,ln):
        b=bin(int(x))[2:]
        return('0'*(ln-len(b))+b)
        
    n=input()
    ln=len(n)
    R=10**10
    for i in range(1,2**(len(n))):
        s=""
        b=bine(i,ln)
        R1=b.count('0')
        if R1<R:
            for j in range(ln):
                if b[j]=="1":
                    s+=n[j]
            if sqr(int(s)) and len(s)==len(str(int(s))) and s!='0':
                R=R1
    if R==10**10:
        print(-1)
    else:
        print(R)