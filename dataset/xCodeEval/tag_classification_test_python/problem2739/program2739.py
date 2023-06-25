def program2739():
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    if (arr[-1] - arr[0]) % 2 == 0:
        d = (arr[-1] - arr[0]) // 2
        valid_values = [arr[-1], arr[0], arr[0] + d]
    else:
        d = arr[-1] - arr[0]
        valid_values = [arr[-1], arr[0]]
    for i in arr:
        if i not in valid_values:
            d = -1
            break
    print(d)