def program3327():
    n = int(input())
    a = input()
    f = 0
    s = 0
    for i in range(1, n):
        if a[i] == 'S'and a[i - 1] == 'F':
            f += 1
        elif a[i] == 'F' and a[i - 1] == 'S':
            s += 1
    if s > f:
        print("YES")
    else:
        print("NO")