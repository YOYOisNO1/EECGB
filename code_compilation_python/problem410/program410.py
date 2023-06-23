def program410():
    n,m=input().split()
    flag =1
    for x in range(n/2+n%2,n+1):
        if(m%x == 0) :
            print x
            flag=0
            break
    if(flag) print -1