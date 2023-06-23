def program51():
    n=int(input())
    a=n
    i=-1
    while abs(i)<len(str(a)):
        while(str(a)[i]!='9'):
            a=a-1
        i-=1
    b=n-a
    print(sum(list(map(int,list(str(a)))))+sum(list(map(int,list(str(b))))))