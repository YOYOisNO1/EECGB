def program1171():
    a,b,c=map(int,input().split())
    if a==b: print('YES')
    elif c==0: print('NO')
     elif (b-a)//c==(b-a)/c and (b-a)//c>0: print('YES')
    else: print('NO')