def program4836():
    n = int(input())
    total = 0
    for i in range(0,n):
        a = list(map(int, input().split()))
        if i != int(n/2):
            total = total + a[i] + a[int(n/2)] + a[n-i-1]
        else:
            total = total + sum(a)
    print(total)