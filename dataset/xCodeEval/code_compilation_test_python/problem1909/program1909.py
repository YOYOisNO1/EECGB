def program1909():
    
     a=list(input())
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    for i in range(len(b)):
        if (ord(b[i])-ord('a'))!=i:
            exit(print('NO'))
    print('YES')