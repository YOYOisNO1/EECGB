def program3900():
    a = int(input())
    b = int(input())
    a, b = min(a, b), max(a, b)
    c = (a + b) // 2
    print((c - a)*(c - a + 1) // 2 + (b - c)*(b - c + 1) // 2)