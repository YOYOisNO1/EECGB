def program97():
    f = [int(x) for x in input().split()]
    n = int(input())
    
    for i in range(2, n):
        f.append(f[i - 1] - f[i - 2])
    print(f[-1] % 1000000007)