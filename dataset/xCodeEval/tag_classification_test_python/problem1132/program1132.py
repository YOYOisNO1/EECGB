def program1132():
    n = int(input())
    days = [int(i) for i in input().split()]
    d = days.copy()
    s = sum(days)
    add = 0
    for i in range(n):
        add += 1
        if n > s:
            d.extend(days)
            s = sum(d)
        else:
            break
    count = 0
    for i in range(n):
        if d[count] == 0:
            for j in range(count,7*add):
                if d[j] == 0:
                    count += 1
                else:
                    count = j
                    break
        d[count] -= 1
    print((count%7)+1)