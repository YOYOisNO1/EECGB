def program644():
    a,b=map(int,input().split())
    r=[b]
    while b>a:
        if b%10==1:
            b=b//10
            r.append(int(b))
        else:
            b=b/2
            r.append(int(b))
    if r[len(r)-1]==a:
            print('YES')
            print(len(r))
            print(*r[::-1])
    else:
            print('NO')