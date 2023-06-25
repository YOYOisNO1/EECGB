def program2289():
    n = int(input())
    tmp = n
    ans = []
    if n == 0:
        print('O-|-OOOO')
        quit()
    while tmp:
        dig = tmp%10
        tmp //= 10
        s = ""
        if (dig >= 5):
            s = "-O|"
        else:
            s = "O-|"
        if (dig < 5):
            rem = int(dig)
        else:
            rem = int(dig - 5)
        s += ('O'*rem)
        s+= '-'
        s += ('O'*(4-rem))
        ans.append(s)
    for a in ans:
        print(a)