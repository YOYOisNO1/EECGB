def program6417():
    arr = [2,4]
    n,m = map(int,input().split(" "))
    for i in range(2,max(n,m)):
        arr.append(arr[i-1]+arr[i-2])
    print((arr[n-1]+arr[m-1]-2)%(10**9+7))