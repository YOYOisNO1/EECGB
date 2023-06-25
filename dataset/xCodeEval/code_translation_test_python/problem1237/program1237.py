def program1237():
    x,y,z,t1,t2,t3=map(int,input().split(' '))
    st=abs(x-y)*t1
    ev=t2*(abs(z-x)+abs(x-y))+t3*3
    if st<ev:
        print('NO')
    else:
        print('YES')