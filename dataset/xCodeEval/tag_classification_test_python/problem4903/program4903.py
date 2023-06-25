def program4903():
    x = int(input())
    arr = [0] * (x+1)
    res=x
    for i in range(2, x+1):
        if arr[i]==0:
            for j in range(i+i, x+1, i):
                arr[j] = i
        arr[i]=i-arr[i]+1;
    for i in range(arr[x],x+1):
        res=min(res, arr[i])
    print(res)