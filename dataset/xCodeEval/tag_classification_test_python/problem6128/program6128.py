def program6128():
    x1,y1,x2,y2 = list(map(int,input().split()))
    arr = [min(abs(x1-x2),1) + min(abs(y1-y2),1),0,max(abs(y2-y1),abs(x2-x1))]
    if ((x1&1^y1&1)==(x2&1^y2&1)):
        if ( abs(x1-x2) == abs(y1-y2) ):
            arr[1] = 1
        else:
            arr[1]= 2
    print(*arr)