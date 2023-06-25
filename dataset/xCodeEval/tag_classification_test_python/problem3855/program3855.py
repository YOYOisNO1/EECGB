def program3855():
    input()
    a=str(input())+'D'
    lst=[]
    c=0
    for i in a:
        if i=='B':
            c=c+1
        else:
            if c>0:
                lst.append(c)
            c=0
    print(len(lst))
    print(*lst)