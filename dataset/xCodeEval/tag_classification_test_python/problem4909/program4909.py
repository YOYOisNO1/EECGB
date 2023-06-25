def program4909():
    n=int(input())
    a=list(map(int,input().split()))
    c1=c2=c3=0
    for i in range(0,n,3):
        c1+=a[i]
    for i in range(1,n,3):
        c2+=a[i]
    for i in range(2,n,3):
        c3+=a[i]
    
    if(c1==max(c1,c2,c3)):
        print('chest')
    elif(c2==max(c1,c2,c3)):
        print('biceps')
    elif(c3==max(c1,c2,c3)):
        print('back')