def program157():
    n=int(input())
    c=0
    while n!=0:
        r=n%10
        if r==4 or r==7:
            c=c+1
        n=n//10
    if c==4 or c==7:
        print('YES')
    else:
        print('NO')