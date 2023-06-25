def program172():
    a, b = map(int, input().split())
    count = 0
    flag = 1
    while a != 1 and b != 1:
        if a == b:
            flag = 0
            break
        if a < b:
            b = b - a
            count += 1
        else:
            a = a - b
            count += 1
    if flag == 0:
        print count + 1
    else:
        print count + max(a, b)