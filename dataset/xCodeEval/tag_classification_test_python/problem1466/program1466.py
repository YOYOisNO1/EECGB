def program1466():
    a,b,c=map(int,input().split(' '))
    #print(a,b,c)
    if (a-b+c)%2==0 and (a+b-c)%2==0 and (b+c-a)%2==0:
        z=(a-b+c)//2
        x=(a+b-c)//2
        y=(b+c-a)//2
        if int(x)==x and int(y)==y and int(z)==z and x>=0 and y>=0 and z>=0:
            print(x,y,z)
            exit()
    print('Impossible')