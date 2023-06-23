def program2176():
    #After seeing the editorials :'(
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a=sorted(a,reverse=True)
    for i in range(1,n+1):
        s=0
        for j in range(n):
            s+=max(0,a[j]-(j//i))
        if s>=m:
            print(i)
            flag=1
            break
    if flag==0:
        print(-1)