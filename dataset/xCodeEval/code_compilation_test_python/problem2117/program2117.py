def program2117():
    a = input().split()
    n, d = int(a[0]), int(a[1])
    a = [int(x) for x in input().split()]
    m = int(input())
    a.sort()
    sum = 0
    for i in [x in range(m) if x < n]:
        sum += a[i]
    sum -= (m-i-1)*d
    print(sum)