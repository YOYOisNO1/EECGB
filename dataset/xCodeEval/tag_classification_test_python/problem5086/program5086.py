def program5086():
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    count1=arr.count(1)
    count2=arr.count(-1)
    ans=0
    for i in range(n):
        l=i
        count1x=0
        count2x=0
        for j in range(i-k,-1,-k):
            if(arr[j]==1):
                count1x+=1
            else:
                count2x+=1
        for j in range(i,n,k):
            if(arr[j]==1):
                count1x+=1
            else:
                count2x+=1
        ans=max(ans,(abs(count1-count1x+count2x-count2)))
    print(ans)