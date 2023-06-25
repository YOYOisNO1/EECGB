def program501():
    args = input().split()
    arr = [int(e) for e in args]
    a = arr[0]; b = arr[1]; c = arr[2]
    res = 0
    current = a
    x = min(b,c)
    for i in range(1, x):
        res += 2 * current
        current += 1
    res += current * (max(b,c) - x + 1)
    print(res)