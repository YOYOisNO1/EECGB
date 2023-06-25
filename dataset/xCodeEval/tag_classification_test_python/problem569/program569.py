def program569():
    n = int(input())
    sum = 0
    x = 0
    a = input().split()
    for i in range(n):
        a[i] = int(a[i])
        sum += a[i]
        x = max(x , a[i])
    while sum > (x * n - 1) // 2:
        x += 1
    print(x)