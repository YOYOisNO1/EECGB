def program1128():
    n = int(input())
    days = [int(x) for x in input().split()]
    i = 0
    while n>0:
        i += 1
        if i > 7:
            i = 1
        n -= days[i - 1]
    print(i)