def program1153():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    e=int(input())
    f=int(input())
    arr3=[e,f]
    i=max(arr3)
    sumd=0
    if(i==e):
        arr2=[a,d]
        u=min(arr2)
        arr=[b,c,d-u]
        k=min(arr)
        sumd=u*e+k*f
    elif(i==f):
        arr=[b,c,d]
        k=min(arr)
        arr=[a,d-k]
        u=min(arr)
        sumd=u*e+k*f
    
    print(sumd)