def program4840():
    n=int(input())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    d=list(zip(*l))
    s=sum(l[(n-1)//2])+sum(d[(n-1)//2])
    for i in range(n):
        s+=l[i][i]+l[i][n-1-i]
    print(s-((3)*l[n//2][n//2]))