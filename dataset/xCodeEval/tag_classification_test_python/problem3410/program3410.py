def program3410():
    z=int(input())
    x=list(map(int,input().split()))
    v=x.copy()
    #print('v=',v)
    b=0
    s=1000
    for i in range(1,z-1):
        v.remove(v[i])
       # print('v=',v)
        for j in range(z-2):
          #  print('v[j+1]=%d         v[j]=%d'%(v[j+1],v[j]))
            if v[j+1]-v[j]>b:
                b=v[j+1]-v[j]
           #     print('b=',b)
        if b<s:
            s=b
          #  print('s=',s)
        v=x.copy() 
        b=0
        #print('*************************')        
    print(s)