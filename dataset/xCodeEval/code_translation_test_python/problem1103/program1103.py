def program1103():
    n=int(input())
    s1=0
    s2=0
    l=list(map(int,input().split()))
    for i in range(n):
        if l[i]>=0:
            s1+=l[i]
        else:
            s2+=l[i]
    print(s1-s2)