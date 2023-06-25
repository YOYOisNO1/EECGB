def program3389():
    for _ in range(int(input())):
            n, k, d = map(int, input().split())
            a = input().split()
            print(min([len(set(a[i:i+d])) for i in range(n-d+1)] or [d]))