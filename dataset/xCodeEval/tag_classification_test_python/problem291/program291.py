def program291():
    inputs = input().split()
    t=int(inputs[0])
    s=int(inputs[1])
    x=int(inputs[2])
    
    if ((x-t)%s==0 or (x-t)%s==1) and x-t!=1 and x>=t:
        print('YES')
    else:
        print('NO')