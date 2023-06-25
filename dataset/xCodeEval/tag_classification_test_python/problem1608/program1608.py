def program1608():
    p = input()
    list = ['H','Q','9']
    x=0
    for i in range(len(p)):
        if p[i] in list:
            print('YES')
            x=1
            break
    if x!=1:
        print('NO')