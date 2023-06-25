def program264():
    str = str(input())
    ss = str.split(' ')
    a = ss[0]
    b = ss[1]
    ans = a + b
    m = ""
    n = ""
    for i in a:
        m += i
        for j in b:
            n += j
            if ans > m + n:
                ans = m + n
        n = ""
    print(ans)