def program710():
    from math import ceil,sqrt
    n = int(input())
    s = input()
    div = []
    for i in range(2,ceil(sqrt(n))+1):
        if n%i == 0:
            div.append(i)
            div.append(n//i)
    div = sorted(list(set(div)))
    for i in div:
        a = s[:i]
        s = a[::-1] + s[i:]
    if n != 2:
        print(s[::-1])
    else:
        print(s)