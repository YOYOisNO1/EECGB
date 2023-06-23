def program187():
    x, y = [int(k) for k in input().split(' ') if k]
    y -= 1
    if x < y:
        print("No")
    else:
        if (x - y) % 2 == 0:
            print("Yes")
        else:
            print("No")