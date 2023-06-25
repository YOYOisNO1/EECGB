def program3379():
    n = int(input())
    s = 1
    for i in range(1, n):
        s += 4 * i
    print(s)