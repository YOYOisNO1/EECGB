def program566():
    n = int(input())
    arr = list(map(int,input().strip().split()))
    k = max(arr)
    while True:
        s = sum(arr)
        if k*n > 2*s:
            print(k)
            break
        else:
            k+=1