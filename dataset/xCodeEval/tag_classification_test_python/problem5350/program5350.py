def program5350():
    s= input()
    s1 =set(s)
    #print(s)
    l = list(s)
    l2=[]
    for i in range(len(l)):
        if l[i] in s1:
            l2.append(l[i])
            s1.remove(l[i])
    #print(l2)
    k = ''.join(l2)
    m = ''.join(sorted(l2))
    c=0
    haha = ord('a')
    #print(haha)
    for i in range(len(k)):
        if(ord(k[i])==haha):
            c+=1
            haha+=1
    
    if(c==(len(k))):
        print("YES")
    else:
        print("NO")
    #if k==m and s[0]=='a':
    #    print("YES")
    #else:
    #    print("NO")
    