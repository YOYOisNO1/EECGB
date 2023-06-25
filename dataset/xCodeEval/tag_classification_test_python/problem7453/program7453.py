def program7453():
    a = [1,3,15,133,2025,37851,1030367,36362925]
    n = int(input())
    if n % 2 == 0:
        print(0)
    else:
        s = a[n / 2];
        for i in range(1, n + 1):
            s = s * i % 1000000007
        print(s)
    