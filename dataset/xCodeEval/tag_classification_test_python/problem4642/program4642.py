def program4642():
    n, k = map(int, input().split())
    s = input()
    arr = dict()
    arr_ = dict()
    ans = 'NO'
    for i in range(65, 91):
        arr[chr(i)] = 0
        arr_[chr(i)] = 0
    for i in s:
        arr_[i] += 1
    for i in s:
        if arr[i] == 0:
            k -= 1
        arr[i] += 1
        if k < 0:
            ans = 'YES'
        if arr[i] == arr_[i]:
            k += 1
    print(ans)