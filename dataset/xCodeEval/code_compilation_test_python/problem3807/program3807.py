def program3807():
    n=int(input())
    vis=[]
    for i in range(5):
        vis.append(0)
    for i in range(n):
        a,b=map(int,input().split())
        vis[a-1]+=1
        vis[b-1]+=1
    count=0
    for i in vis:
        if i<=1:
            count+=1
    if count>=3 or n>=3:
        print("WIN")
    else:
        print("FAIL")
    
    