def program7352():
    n,m=map(int,input().split(" "))
    if n==1 or m==1:
        print((((n*m)//6)*6)+((n*m)%6>3)*((((n*m)%6)%3)*2))
        
    elif n*m<6:
        print(0)
        
    elif n*m==6:
        print(4)
    elif n*m==14:
        print(12)
    # elif (n==2 and m%2==1) or (m==2 and n%2==1):
    #     print(n*m-2)
    # elif((n==2 and m%2==0) or (m==2 and n%2==0)):
    #     print(n*m)
    else:
        print(n*m-(n*m)%2)
        