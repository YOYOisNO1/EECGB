def program1651():
    n=input()
    s=input()
    l=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']
    if(n=="R"):
        for i in s:
            p=l.index(i)
            print(l[p-1],end='')
    else:
        for i in s:
            p=l.index(i)
            print(l[p+1],end='')