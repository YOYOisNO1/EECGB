def program139():
    n = int(input())
    temp = []
    while n >= 10:
        x = n % 10
        temp.append(min(x,9-x))
    if n != 9:
        temp.append(min(n,9-n))
    else:
        temp.append(n)
    res = 0
    for i in range(len(temp)):
        res += temp[i]*(10**i)
    print(res)