def program2472():
    n = int(input())
    s = input()
    b = 0
    d = 0
    max_d = 0
    m = False
    k = 0
    for i in range(n):
        if s[i] == '(':
            b += 1
        elif s[i] == ')':
            b -= 1
        if b == 0:
            if s[i] == '_' or s[i] == ')' or s[i] == '(':
                if d > max_d:
                    max_d = d
                d = 0
            else:
                d += 1
        else:
            if s[i] == '_' or s[i] == ')' or s[i] == '(':
                m = True
            else:
                if m:
                    k += 1
                    m = False
    if d > max_d:
        max_d = d
    print(max_d, k)