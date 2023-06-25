def program1142():
    n = int(input())
    a = [int(i) for i in input().split()]
    
    ones = 0
    point = 0
    best = 0
    for i in range(n):
        ones += a[i]
        if (a[i] == 1):
            if (point > 0):
                point -= 1
            else:
                point = 0
        else:
            point += 1
        best = max(best, point)
    if (ones == n):
        print((n) - 1)
    else:
        print((ones) + best)