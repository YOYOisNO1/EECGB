def program3725():
    n,d=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    max=0
    for i in range(len(arr)):
        count=0
        for j in range(i,len(arr)):
            if arr[j]-arr[i]<=d:
                count+=1
        if max<count:
            max=count
    print(len(arr)-max)
                