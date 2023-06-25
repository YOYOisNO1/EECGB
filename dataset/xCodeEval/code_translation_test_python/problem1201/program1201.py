def program1201():
    r, l, x, y, k = map(int, input().split())
    for i in range(x, y + 1):
        if k * i in range(r, l + 1):
            print("YES")
            break
    else:
        print("NO")