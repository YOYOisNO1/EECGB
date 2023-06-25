def program555():
    x = list(map(int, input().split()))
    y = min(x)
    s = 0
    if x[0] == y:
        if y == x[1] and y == x[2]:
            s+=y*3-3
        if y == x[1]:
            s+=y*3
        else:y[1] == y[2]:
            s+=y*3+3
    elif x[1] == y:
        if y == [2]:
            s+=y*3-3
        else:
            s+=y*3
    else:
        s+=y*3-3
    print(s)
            