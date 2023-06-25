def program567():
    n = int(input())
    a = list(map(int, input().split()))
    sume = sum(a)
    sumw = 0
    maxa = max(a)
    for i in range(n):
        sumw += abs(maxa - a[i])
    while sumw <= sume:
        sumw = 0
        for i in range(n):
            sumw += abs(maxa - a[i])
        if sumw > sume:
            break
        maxa += 1
    print(maxa)