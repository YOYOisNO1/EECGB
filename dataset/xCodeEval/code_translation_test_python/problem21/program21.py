def program21():
    #CF 393 yl1
    # Petr
    #n=int(input())
    
    m,d=list(map(int,input().split()))
    
    if m==2:
        n=28
    elif m in {1,3,5,7,8,10,12}:
        n=31
    else:n=30
    #{1,3,5,8,10,12}
    # for i in range(n):
    n+=d-1
    if n%7==0:
        n=n//7
    else:
        n=n//7+1
    print(n)