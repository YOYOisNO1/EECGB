def program1652():
    key=input()
    str=input()
    a=['q','w','e','r','t','y','u','i','o','p']
    b=['a','s','d','f','g','h','j','k','l',';']
    c=['z','x','c','v','b','n','m',',','.','/']
    if key=='R':
        for i in str:
            if i in a:
                print(a[a.index(i)-1],end='')
            elif i in b:
                print(b[b.index(i)-1],end='')
            elif i in c:
                print(c[c.index(i)-1],end='')
            else:
                print(i,end='')
    else:
        for i in str:
            if i in a:
                print(a[a.index(i)+1],end='')
            elif i in b:
                print(b[b.index(i)+1],end='')
            elif i in c:
                print(c[c.index(i)+1],end='')
            else:
                print(i,end='')