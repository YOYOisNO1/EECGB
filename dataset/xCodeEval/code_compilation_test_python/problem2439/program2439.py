def program2439():
    step = 1
    i = 0
    n = int(input())
    while (i < n) :
        i += step
        step += 1
    if (i == n) :
        print("YES")
    else :
        print("NO")
        