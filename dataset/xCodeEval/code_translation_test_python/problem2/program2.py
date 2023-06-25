def program2():
    k=int(input())
    l=int(input())
    if l%k==0:
        i=0
        while k**i<l:
            i+=1
        if k**i==l:
            print('YES')
            print(i-1)
        else:
            print('NO')
    else:
        print('NO')