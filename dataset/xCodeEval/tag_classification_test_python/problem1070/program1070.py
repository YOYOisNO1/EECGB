def program1070():
    import sys, os.path
    from collections import*
    from copy import*
    import math
    mod=10**9+7
    if(os.path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    
    n=int(input())
    r1,s1,p1=map(int,input().split())
    r2,s2,p2=map(int,input().split())
    m1=0
    m1+=min(r1,s2)+min(p1,r2)+min(s1,p2)
    a=min(r1,r2+p2)
    b=min(p1,p2+s2)
    c=min(s1,s2+r2)
    m3=min(r2,r1)+min(p2,p1)+min(s2,s1)
    print(n-a-b-c,m1)