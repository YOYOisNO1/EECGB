def program470():
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    if  a.count(100)%2==0:
        if a.count(200)%2==0:
            print('YES')
        elif a.count(100)>0:
            print('YES'       )
        else:
            print('NO')    
    else:
        print('NO')