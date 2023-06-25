def program1739():
    n = int(input())
    if(n<=3):
        print(n+1)
    else:
        a = n**0.5
        d = a-int(a)
        if(d>=0.5):
            a = int(a)+1
            print(2*a)
        else if(d>0 and d<0.5):
            a = int(a)
            print(2*a+1)
        else:
            a = int(a)
            print(2*a)