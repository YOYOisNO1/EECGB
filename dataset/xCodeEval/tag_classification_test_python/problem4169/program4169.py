def program4169():
    
    n,a=map(int,input().split())
    '''
    l1=[i for i in range(1,n,2)]
    l2=[i for i in range(n,0,-2)]
    print(l1)
    print(l2)
    if a in l1:
        print(l1.index(a)+1)
    else:
        print(l2.index(a)+1)'''
    if a%2==0:
        dist=(n-a)//2  
        print(dist+1)
    else:
        print(a//2+1)