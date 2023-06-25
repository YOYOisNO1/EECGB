def program414():
    z=input().split(' ')
    n=int(z[0])
    m=int(z[1])
    min=int(n/2) if(n%2==0) else int(n/2)+1
    if(m<=n && m>=min):
        while(true):
            if(min%m==0):
                print(str(min))
                break
            else:
                min+=1
    else:
        print ("-1")