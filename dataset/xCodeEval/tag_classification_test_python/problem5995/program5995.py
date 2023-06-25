def program5995():
    a=list(map(int,input().split()))
    b=a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
    y=0
    t=0
    for i in range(6):
        for j in range(6-(abs(i-6))+1,6):
            for k in range(6-(abs(j-6))+1,6):
                if (a[i]+a[j]+a[k])==(b//2) and (b%2==0):
                    print('YES')
                    y+=1
                    break
            if y>0:
                break
        if y>0:
            break
    else:
        print('NO')