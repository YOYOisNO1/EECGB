def program1524():
    n = int(input())
    m = 1000000007
    res = 1
    for i in range(1, n):
        res = (res * (n+i) * pow(i, m-2, m)) % m;
    print((2*res-n)%m)