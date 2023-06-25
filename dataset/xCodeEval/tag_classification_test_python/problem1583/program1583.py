def program1583():
    a, b = map(int, input().split())
    if (a == 0 and b == 0) or abs(a - b) > 1:
        print("NO")
    else:
        print("YES")