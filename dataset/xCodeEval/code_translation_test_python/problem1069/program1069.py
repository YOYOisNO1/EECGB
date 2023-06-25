def program1069():
    n, k = map(int, input().strip().split())
    if (n / k) % 2 == 1:
        print("YES")
    else:
        print("NO")