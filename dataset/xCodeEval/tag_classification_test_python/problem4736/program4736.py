def program4736():
    n = int(input())
    l = sorted(set(map(int, input().split())))
    for i in range(1, len(l) - 1):
        if (l[i + 1], l[i]) == (l[i] + 1, l[i - 1] + 1):
            print("YES")
            exit(0)
    print("NO")