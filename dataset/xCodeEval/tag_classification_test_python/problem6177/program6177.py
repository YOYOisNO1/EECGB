def program6177():
    a,b,c,d=map(int,input().split())
    if a==c or b==d:
        print('1',end=' ')
    else:
        print('2',end=' ')
    if abs(a-c)==abs(b-d):
        print('1',end=' ')
    elif (a-b)%2==0 and (c-d)%2==0:
        print('2',end=' ')
    elif (a-b)%2!=0 and (c-d)%2!=0:
        print('2',end=' ')
    else:
        print('0',end=' ')
    print(max(abs(a-c),abs(b-d)))