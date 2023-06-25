def program2446():
    n=input() 
    s=input().split('(')
    ss=[]
    for x in s :
        ss+=x.split(')')
    A,B = 0,0   
    for i in range(len(ss)):
        if i%2==1:
            for x in ss[i].split('_'):
                B+=len(x)!=0
        else:
            for x in ss[i].split('_'):
                A=max(A,len(x))
    print(A,) B