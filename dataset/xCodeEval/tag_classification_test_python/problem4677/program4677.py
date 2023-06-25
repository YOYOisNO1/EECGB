def program4677():
    n,r=map(int,input().split())
    s=input()
    x={}
    y=set()
    for j in range(n):
        x[s[j]]=j
    for j in range(n):
        y.add(s[j])
        if(len(y)>r):
            print("YES")
            break
        if(j==x[s[j]]):
            y.remove(s[j])
    if(len(y)<=r):
        print("NO")
        