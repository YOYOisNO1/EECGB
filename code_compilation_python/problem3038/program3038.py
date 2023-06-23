def program3038():
    a=input()
    b=input()
    c=input()
    d=input()
    
    if (a[0] == 'X'):
        s1 = a[1]+b
    if (a[1] == 'X'):
        s1 = b[1]+b[0]+a[0]
    if (b[0] == 'X'):
        s1 = a + b[1]
    if (b[1] == 'X'):
        s1 = a + b[0]
    
    if (c[0] == 'X'):
        s2 = c[1]+d
    if (c[1] == 'X'):
        s2 = d[1]+d[0]+c[0]
    if (d[0] == 'X'):
        s2 = c + d[1]
    if (d[1] == 'X'):
        s2 = c + d[0]
    s1=s1+s1
    
    for i in range(0,len(s1)):
       if(s1[i] == s2[0]):
           if((s1[i+1] == s2[1]) and (s1[i+2] == s2[2])):
               print("YES")
               break
           else:
               print("NO")
               break
    a=input()
    b=input()
    c=input()
    d=input()
    
    if (a[0] == 'X'):
        s1 = a[1]+b[1]+b[0]
    if (a[1] == 'X'):
        s1 = b[1]+b[0]+a[0]
    if (b[0] == 'X'):
        s1 = a + b[1]
    if (b[1] == 'X'):
        s1 = a + b[0]
    #print(s1)
    
    if (c[0] == 'X'):
        s2 = c[1]+d[1]+d[0]
    if (c[1] == 'X'):
        s2 = d[1]+d[0]+c[0]
    if (d[0] == 'X'):
        s2 = c + d[1]
    if (d[1] == 'X'):
        s2 = c + d[0]
    #print(s2)
    
    s1=s1+s1
    
    for i in range(0,len(s1)):
       if(s1[i] == s2[0]):
           if((s1[i+1] == s2[1]) and (s1[i+2] == s2[2])):
               print("YES")
               break
           else:
               print("NO")
               break