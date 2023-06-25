def program3236():
    n = int(input())
    k = 0
    for i in range(n):
        l = list(map(int,input().split()))
        k += l[n//2]
        if n != n//2:
        k=k+l[i]+l[-i-1]
    print(k)