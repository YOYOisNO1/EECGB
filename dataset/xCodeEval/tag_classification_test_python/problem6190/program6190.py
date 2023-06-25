    '''input
    5 5 6 6
    '''
    
def bis(a,b,c,d):
        if (a+b)%2 != (c+d)%2:
            print(0,)
        elif abs(a-c) != abs(b-d):
            print(2,)
        else:
            print(1,)
    a,b,c,d=map(int,input().split())
    if a==c or b==d:
        print(1,)
    else:
        print(2,)
    bis(a,b,c,d)
    print(max(abs(a-c),abs(b-d)))