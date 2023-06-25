def program2490():
    s=input()+input()+input()
    for i in [0,1,2,3,4]:
        if (s[i]!=s[8-i]):
            print('NO')
            exit()
    print('YES')