def program3967():
    w, m = map(int, input().split())
    while m:
        if m % w == 1: m = (m - 1) / w
        elif m % w == w - 1: m = (m + 1) / w
        elif m % w == 0: m /= w
        else:
            print("NO")
            break
    else:
        print("YES")