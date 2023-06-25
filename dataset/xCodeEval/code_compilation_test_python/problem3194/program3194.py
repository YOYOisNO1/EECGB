def program3194():
    a= list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    if(b[0]<=a[0]and b[1]<=a[1]):
        if(b[2]>=a[2] and b[3]>=a[3]):
            print('NO')
        elif (b[2]>=a[2]):
            x=a[0]
            y=b[3]
            if(c[0]<=x and c[1]<=y):
                if(c[2]>=a[2] and c[3]>=a[3]):
                    print('NO')
                else:
                    print('YES')
            else:
                print('YES')
        elif b[3]>=a[3]:
            x = b[2]
            y = a[1]
            # print(x,y)
            if (c[0] <= x and c[1] <= y):
                if (c[2] >= a[2] and c[3] >= a[3]):
                    print('NO')
                else:
                    print('YES')
            else:
                print('YES')
        else:
            print('YES')
    elif(c[0]<=a[0]and c[1]<=a[1]):
        if(c[2]>=a[2] and c[3]>=a[3]):
            print('NO')
        elif (c[2]>=a[2]):
            x=a[0]
            y=c[3]
            if(b[0]<=x and b[1]<=y):
                if(b[2]>=a[2] and b[3]>=a[3]):
                    print('NO')
                else:
                    print('YES')
            else:
                print('YES')
        elif c[3]>=a[3]:
            x = c[2]
            y = a[1]
            if (b[0] <= x and b[1] <= y):
                if (b[2] >= a[2] and b[3] >= a[3]):
                    print('NO')
                else:
                    print('YES')
            else:
                print('YES')
        else:
            print('YES')
    else:
        print('YES')
    
    