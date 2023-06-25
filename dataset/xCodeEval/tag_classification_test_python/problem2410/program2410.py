    n=int(input())
    s=input()
def f1(last,i):
        global s
        m=0
        for k in s[last:i].split('_'):
            m=max(len(k),m)
        return m
def f2(last,i):
        global s
        m=0
        for k in s[last:i].split('_'):
            if k!='': m+=1
        return m
    a1=0
    a2=0
    last=0
    i=0
    while i<n:
        if s[i]=='(':
            a1=max(f1(last,i),a1)
            last=i+1
            while s[i]!=')':
                i+=1
            a2+=f2(last,i)
            last=i+1
        i+=1
    a1=max(f1(last,n),a1)
    print(a1,a2)