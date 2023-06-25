def program6180():
    a,b,c,d=map(int,input().split())
    e=[0,0,0]
    if a==c or b==d:e[0]=1
    else:e[0]=2
    if abs(a%2-b%2)!=abs(c%2-d%2):e[1]=0
    elif abs(a-c)==abs(b-d):e[1]=1
    else:e[1]=2
    e[2]=max(abs(a-c),abs(b-d))
    print(' '.join(map(str,e)))