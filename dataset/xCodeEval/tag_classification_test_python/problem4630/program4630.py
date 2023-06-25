def program4630():
    n,k=map(int,input().split())
    l=list(input())
    d={}
    for i in range(n):
        d[l[i]]=[0,i]
    ac=0
    for i in range(n):
        if d[l[i]][0]==0:
            ac+=1
            d[l[i]][0]=1
        if ac>k:
            print("YES")
            break
        if d[l[i]][1]==i:
            ac-=1
    else: print("NO")