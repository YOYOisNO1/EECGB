def program7233():
    import sys,math,string,bisect
    input=sys.stdin.readline
    from collections import deque
    L=lambda : list(map(int,input().split()))
    Ls=lambda : list(input().split())
    M=lambda : map(int,input().split())
    I=lambda :int(input())
    p1,p2,p3,p4,b,a=M()
    k=min(p1,p2,p3,p4)
    c=0
    for i in range(b,min(k,a+1)):
        c+=1
    print(c)