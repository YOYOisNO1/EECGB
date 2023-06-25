def program24():
    
    arr =[[0 for _ in range(5)] for _ in range(5)]
    # print(arr)
    for i in range(5):
        arr[i] = list(map(int,input().split()))
        if 1 in arr[i]:
            for j in range(5):
                if arr[i][j] == 1:
                    posI = i
                    posJ = j
    print(abs(posI-2)+abs(posJ-2))    
        