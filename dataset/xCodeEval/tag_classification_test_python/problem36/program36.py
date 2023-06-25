def program36():
    a=input()
    a=a.split()
    a=[int(i) for i in a]
    flag=0
    a.sort()
    for _ in range(1):
        if a[0] + a[1]==a[2]+a[3]:
            flag=1
            break
        if a[0] + a[2]==a[1]+a[3]:
            flag=1
            break
        if a[0] + a[3]==a[2]+a[1]:
            flag=1
            break
        if a[0]+a[1]+a[2]==a[3]:
            flag=1
            break
    
    if flag==0 :
        print("NO")
    else :
        print("YES")
            