def program2598():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        if n % 2 == 0 and m % 2 == 0:
            print("YES" if k % 2 == 0 else "NO")
        elif n % 2 == 0 and m % 2 == 1:
            print("YES" if k % 2 == 0 and k <= n * (m - 1) // 2 else "NO")
        elif n % 2 == 1 and m % 2 == 0:
            if k >= (m // 2) and (k - (m // 2)) % 2 == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO" if k != 0 else "YES")