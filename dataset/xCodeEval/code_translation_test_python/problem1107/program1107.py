def program1107():
    [n,l]=[int(i) for i in str(input()).split(' ')]
    
    r1=[int(i) for i in str(input()).split(' ')]
    r2=[int(i) for i in str(input()).split(' ')]
    
    for k in range(l):
        tmp=[(k+i)%l for i in r1]
        if all(i in r2 for i in tmp):
            tmp=False
            break;
    if tmp==False:
        print("YES")
    else:
        print("NO")