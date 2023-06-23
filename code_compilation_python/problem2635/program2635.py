def program2635():
    c=int(input("c:")
    v0=int(input("v0:")
    v1=int(input("v1:")
    a=int(input("a:")
    l=int(input("l:")
    page=0
    arr=[]
    for i in range(1000):
        page+=v+(i*a)
        if i>0:
            page+=v+(i*a)+l
        arr.append(i)
        if page>=c:
            break
        if page >=vm:
            for i in range(1000):
                page+=page
                arr.append(i)
                if page>=c:
                    break
                
         print(len(arr))   
            