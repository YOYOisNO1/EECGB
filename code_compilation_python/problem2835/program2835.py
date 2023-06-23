def program2835():
    vn=input()
    m=input()
    lst=[]
    for i in range(len(n)):
        if n[i]=='1' and m[i]=='0':
            lst.append(1)
        elif n[i]=='0' and m[i]=='1':
            lst.append(1)
        else:
            lst.append(0)
        
    for i in lst:
        print(i,sep="",end="