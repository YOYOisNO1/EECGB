def program2523():
    n = int(input())
    a = list(map((int, input().split()))
    b = sorted(a)
    res = 0
    for i in range(n/2):
        res += b[i*2+1]-b[i*2]
    print(res)