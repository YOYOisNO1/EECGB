def program386():
    a = [int x for x in input().split()]
    for i in range (6):
        for i1 in range (i, 6):
            for i2 in range (i1, 6):
                if a[i] + a[i1] + a[i2] == a[5-i] + a[5-i1] + a[5-i2]:
                    print("YES")
                    exit(0)
    print("NO")