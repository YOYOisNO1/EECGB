def program310():
    
    ab= input().split()
    a= int(ab[0])
    b= int(ab[1])
    test=[]
    for i in range(1,a+1):
        test.append(i)
    
    c= b//a
    c=c+1
    test= test*c
    k=0
    while b-test[k]>=0:
        b=b-test[k]
        k=k+1
    
    print(b)