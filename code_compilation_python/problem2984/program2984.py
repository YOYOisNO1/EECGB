def program2984():
    n = int(input())
    a = [int(x) for x in input().strip().split(' ')]
    for i, x in enumerate(a):
        if x == 29:
            a[i] = 28
    b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    c = b * 10
    
    flag = False
    for i in range(len(c):
        if a == c[i:i + len(a)]:
            flag = True
    
    if flag == True: print("Yes")
    else: print("No")