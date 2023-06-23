def program3500():
    n,k = map(int,input().split())
    if(k==1):
        print("Yes")
    elif(k>100 || k>=n):
        print("No")
    else:
        for i in range(1,k+1):
            if((n+1)%i != 0):
                print("No")
                return
        print("Yes")