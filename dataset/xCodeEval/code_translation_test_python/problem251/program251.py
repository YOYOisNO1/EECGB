def program251():
    n=input()
    a=input()
    lis=[]
    for i in a:
        if i=='9':
            lis.append(7)
            lis.append(3)
            lis.append(3)
            lis.append(2)
        if i=='8':
            lis.append(2)
            lis.append(2)
            lis.append(2)
            lis.append(7)
        if i=='7':
            lis.append(7)
        if i=='6':
            lis.append(3)
            lis.append(5)
        if i=='5':
            lis.append(5)
        if i=='4':
            lis.append(2)
            lis.append(2)
            lis.append(3)
        if i=='3':
            lis.append(3)
        if i=='2':
            lis.append(2)
    lis.sort(reverse=True)
    for i in range(len(lis)):
        lis[i]=str(lis[i])
    print('').join(lis)
            