def program2205():
    a, b, s = map(int, input().split(" "))
    a = abs(a)
    b = abs(b)
    s = abs(s)
    print("Yes" if (a + b - s) <= 0 and (a + b - s) % 2 ==  0 else "No")