def program2790():
    a = [0]*3001
    a[0]=a[1]=1
    
    for i in range(2,3001):
        if a[i]==0:
            for j in range(i+i,3001,i):
                a[j]+=1
    c = 0
    for i in range(int(input())+1):
        if a[i]==2:
            c+=1
    print(c)