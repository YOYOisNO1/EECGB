def program2771():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    excess,count=0,0
    for i in range(n):
        if a[i]===1 and b[i]==0:
            count+=1
        if a[1]==0 and b[1]==1:
            excess+=1
    if excess==0:
        print(-1)
    elif count>excess:
        print(1)
    else:
        print(excess//count+1)