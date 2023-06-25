def program4289():
    t = str(input())
    n = 0
    m = len(t)-(len(t)//2+1)
    for i in range(1,m+1):
            s = t[0:len(t)-i:1]
            for j in range(len(t)-i):
                    d = t[j+1:len(t):1]
                    if s == d:
                            n = 1
                            print('YES')
                            print(s)
                    elif n == 1:
                            break
    if n != 1:
            print('NO')