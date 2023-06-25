def program300():
    n = int(input())
    for i in range(91):
        out = -1
        summ = 0
        s = int(i*i + 4*n)
        root = int(s**0.5)
        if root * root == s:
            out = (- i + int(root))//2
            h = i
            break
    c = out
    while out > 0:
        m = out%10
        summ += m
        out //= 10
    if int(summ) == i and c >= 0:
        print(c)
    else:
        print(-1)