def program4061():
    n = int(input())
    a = []
    for i in range(n):
        b = int(input())
        a.append(b)
    c = list(set(a))
    if len(c) != 2:
        print("NO")
    else:
        k = 0
        for i in range(len(a)):
            if a[i] == c[0]:
                k += 1
        if k == len(a) // 2:
            print("YES")
            print(c[0],c[1])
        else:
            print("NO")