def program6115():
    a,b,c,d = map(int,input().split())
    e= [0]*3
    if a==c:
        e[0] = str(1)
        e[2] = str(abs(b-d))
        if abs(b-d)%2==0:
            e[1]='2'
        else:
            e[1] ='0' 
        print(' '.join(e))
    elif b==d:
        e[0] = str(1)
        e[2] = str(abs(a-c))
        if abs(a-c)%2==0:
            e[1]='2'
        else:
            e[1] ='0' 
        print(' '.join(e))
    else:
        e[0] = '2'
        e[2] =str( max(abs(c-a),abs(d-b)))
        if (a+b)%2 == (c+d)%2:
            if abs(c-a)==abs(b-d):
                e[1] = '1'
            else:
                e[1]='2'
        else:
            e[1] ='0'
        print(' '.join(e))
                