def program4708():
    from collections import defaultdict
    n,k=map(int,input().split())
    s=input()
    d=defaultdict(lambda:[-1,-1])
    s1=s[::-1]
    for x in range(65,91):
        if s.find(chr(x))!=-1:
            d[chr(x)][0]=s.find(chr(x))
            d[chr(x)][1]=(n-1)-s1.find(chr(x))
    t=s[0]
    k1=1
    f=0
    for x in range(1,n):
        if s[x]!=t and d[s[x-1]][1]!=x-1 and d[s[x]][0]==x:
            k1+=1
            if k1>k:
                f=1
                break
        elif d[s[x]][0]!=x and d[s[x-1]][1]==x-1:
            k1-=1
        t=s[x]
    if f:
        print("YES")
    else:
        print("NO")
            
        