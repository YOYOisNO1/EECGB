def program1163():
    n = int(input());s=n
    arr =[ ]
    while (True):
        for i in range(0,s+3):
            if (i*(i-1)*(1/2)<=n):continue
            else :
                arr.append(i-1);n-=(i-1)*(i-2)*(1/2);break
        if (n<=0):break
    j=0
    for i in 'abcdefghijklmnobqrstuvwxyz':
        while (arr[j]!=0):print(i,end='');arr[j]-=1
        j+=1
        if (j==len(arr)):break
    
    