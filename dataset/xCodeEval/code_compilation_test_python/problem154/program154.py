def program154():
    n=int(input())
    arr=[0]*(n+1)
    arr[0]=0
    arr[1]=0 
    arr[2]=0
    x=(n)//2
    for i in range(2,x+1):
        if arr[i]==0:
            j=2
            while(i*j<=n):
                arr[i*j]+=1 
                j+=1 
    output=0
    for i in arr:
        if i==2:
            output+=1 
    print(output)
        